"""LLM manager for handling multiple AI providers (OpenAI, Anthropic) with LangChain"""
import os
from abc import ABC, abstractmethod
from typing import Dict, Any
from config import DEFAULT_MODEL, GPT4_MODEL, DEFAULT_TEMPERATURE, GPT4_TEMPERATURE, PROVIDER


class ModelProvider(ABC):
    """Abstract base class for AI model providers"""
    
    @abstractmethod
    def setup_api_key(self) -> None:
        """Setup API key for the provider"""
        pass
    
    @abstractmethod
    def create_llm(self, model_name: str, temperature: float) -> Any:
        """Create LLM instance for the provider"""
        pass
    
    @abstractmethod
    def get_provider_name(self) -> str:
        """Get the name of the provider"""
        pass


class OpenAIProvider(ModelProvider):
    """OpenAI model provider implementation"""
    
    def setup_api_key(self) -> None:
        """Setup OpenAI API key"""
        if "OPENAI_API_KEY" not in os.environ or not os.environ["OPENAI_API_KEY"].strip() == "":
            print("🔑 OpenAI API key not found in environment variables.")
            api_key = input("Please enter your OpenAI API key: ").strip()
            if not api_key:
                raise ValueError("OpenAI API key cannot be empty!")
            os.environ['OPENAI_API_KEY'] = api_key
            print("✅ OpenAI API key is set successfully!")
        else:
            print("✅ OpenAI API key is already set.")
    
    def create_llm(self, model_name: str, temperature: float) -> Any:
        """Create OpenAI LLM instance"""
        from langchain_community.chat_models import ChatOpenAI
        return ChatOpenAI(model=model_name, temperature=temperature)
    
    def get_provider_name(self) -> str:
        return "OpenAI"


class AnthropicProvider(ModelProvider):
    """Anthropic model provider implementation"""
    
    def setup_api_key(self) -> None:
        """Setup Anthropic API key"""
        if "ANTHROPIC_API_KEY" not in os.environ or not os.environ["ANTHROPIC_API_KEY"].strip() == "":
            print("🔑 Anthropic API key not found in environment variables.")
            print("💡 You can get your API key from: https://console.anthropic.com/")
            api_key = input("Please enter your Anthropic API key: ").strip()
            if not api_key:
                raise ValueError("Anthropic API key cannot be empty!")
            os.environ['ANTHROPIC_API_KEY'] = api_key
            print("✅ Anthropic API key is set successfully!")
        else:
            print("✅ Anthropic API key is already set.")
    
    def create_llm(self, model_name: str, temperature: float) -> Any:
        """Create Anthropic LLM instance"""
        from langchain_anthropic import ChatAnthropic
        return ChatAnthropic(model=model_name, temperature=temperature)
    
    def get_provider_name(self) -> str:
        return "Anthropic"


class ModelProviderFactory:
    """Factory class for creating model providers"""
    
    _providers = {
        'openai': OpenAIProvider,
        'anthropic': AnthropicProvider
    }
    
    @classmethod
    def create_provider(cls, provider_name: str) -> ModelProvider:
        """Create a model provider instance"""
        provider_name = provider_name.lower()
        if provider_name not in cls._providers:
            raise ValueError(f"Unsupported provider: {provider_name}. "
                           f"Supported providers: {list(cls._providers.keys())}")
        return cls._providers[provider_name]()
    
    @classmethod
    def get_supported_providers(cls) -> list:
        """Get list of supported providers"""
        return list(cls._providers.keys())


class LLMManager:
    """Unified LLM manager that works with multiple AI providers"""
    
    def __init__(self):
        self.provider = ModelProviderFactory.create_provider(PROVIDER)
        self.provider.setup_api_key()
        self._llm_cache: Dict[str, Any] = {}
        print(f"✅ LLM Manager initialized with {self.provider.get_provider_name()} provider!")
    
    def get_llm(self, model_name: str = DEFAULT_MODEL, temperature: float = DEFAULT_TEMPERATURE) -> Any:
        """Get LLM instance (cached for performance)"""
        cache_key = f"{model_name}_{temperature}"
        if cache_key not in self._llm_cache:
            try:
                self._llm_cache[cache_key] = self.provider.create_llm(model_name, temperature)
                print(f"✅ Created {self.provider.get_provider_name()} LLM instance: {model_name}")
            except Exception as e:
                raise RuntimeError(f"Failed to create LLM instance: {e}")
        return self._llm_cache[cache_key]
    
    def get_gpt35_llm(self) -> Any:
        """Get default model LLM instance (maintains backward compatibility)"""
        return self.get_llm(DEFAULT_MODEL, DEFAULT_TEMPERATURE)
    
    def get_gpt4_llm(self) -> Any:
        """Get advanced model LLM instance (maintains backward compatibility)"""
        return self.get_llm(GPT4_MODEL, GPT4_TEMPERATURE)
    
    def get_provider_info(self) -> Dict[str, str]:
        """Get information about the current provider"""
        return {
            "provider": self.provider.get_provider_name(),
            "default_model": DEFAULT_MODEL,
            "advanced_model": GPT4_MODEL
        }
