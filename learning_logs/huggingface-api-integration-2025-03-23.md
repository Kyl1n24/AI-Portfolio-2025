# AI Learning Log - March 23, 2025

## Hugging Face API Integration with DeepSeek Model

### Context & Goals

**Context:** Originally using OpenAI (openai library) in Andrew Ng's course practice, but needed to switch to a free API on Hugging Face to avoid costs.

**Goals:** 
- Successfully call a free LLM using Hugging Face in existing Python code structure
- Ensure environment variables load correctly across different project directories
- Confirm model choice is feasible for daily practice

### Issues Encountered & Solutions

#### 1. API Key Configuration
**Issue**: OpenAI client couldn't find the API key, resulting in an error:
```
openai.OpenAIError: The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable
```

**Solution**: 
- Created a `.env` file in the project root directory with the HF API key: `HF_API_KEY=hf_xxxxx`
- Modified the `load_dotenv` call to use relative path pointing to root directory:
```python
# Change from
load_dotenv('.env', override=True)
# To
load_dotenv('../../.env', override=True)  # Navigate up two levels from current directory
```

#### 2. Project Directory Structure
**Issue**: VS Code terminal and file explorer were pointing to the wrong directory (2025-02-17 instead of 2025-03-22).

**Solution**: Opened the entire project folder as a workspace in VS Code to ensure consistent file paths and terminal working directory.

#### 3. Code Structure Modifications
**Issue**: Function documentation inconsistencies between `get_llm_response` and `get_chat_completion`.

**Solution**: Standardized the error handling and documentation style between the two functions. 
See: [helper_functions.py](../daily_progress/2025-03-22/helper_functions.py)

#### 4. OpenAI-compatible Interface vs. Real OpenAI
**Clarification**: Some Hugging Face models provide an OpenAI-compatible interface that allows using the openai library with a custom base_url, without incurring OpenAI fees.

**Solution**: Verified we are correctly using Hugging Face's OpenAI-compatible endpoint with HF API key rather than actual OpenAI endpoints.

### Model Selection Criteria

When selecting free models on Hugging Face, look for:
- Models that display "HF Inference API" or "Hosted inference API" on the model page
- Models that show a quick test interface on the right panel of their page

**Selected Model**: DeepSeek-R1-Distill-Qwen-32B
- Good performance for general question-answering
- Available through Hugging Face's free API tier
- Compatible with OpenAI-style interface

### Implementation Details

#### Model Configuration
Successfully implemented Hugging Face's OpenAI-compatible interface:

```python
# Key code change in helper_functions.py
client = OpenAI(
    base_url="https://router.huggingface.co/hf-inference/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B/v1",
    api_key=hf_api_key
)
```

Full implementation available in:
- [helper_functions.py](../daily_progress/2025-03-22/helper_functions.py)
- [llm_practice.py](../daily_progress/2025-03-22/llm_practice.py)

#### Testing Results
Successfully tested the implementation with a basic question:
```python
print_llm_response("What is the capital of France?")
```

The model correctly responded with a detailed answer about Paris being the capital of France.

### Best Practices Identified

1. **API Key Management**: Store API keys in `.env` files and use `load_dotenv` to load them. Ensure `.env` files are in `.gitignore` to avoid exposing credentials.

2. **Error Handling**: Always implement proper try/except blocks to catch and handle potential errors, especially for API calls that might fail.

3. **Consistent Documentation**: Maintain consistent function documentation style across the codebase.

4. **Path Resolution**: Use relative paths (`../../`) instead of absolute paths to ensure code works across different environments.

5. **Project Organization**: Open entire project folders in VS Code for consistent terminal paths and file navigation.

6. **Documentation Best Practices**: 
   - Link to code files rather than duplicating all code in documentation
   - Include only key code snippets that highlight important changes or concepts
   - Use standard YYYY-MM-DD format in filenames for chronological organization

### Next Steps

1. Continue with Andrew Ng's coursework, adapting examples to work with Hugging Face models
2. Implement more sophisticated prompts for the coffee analysis project
3. Consider expanding the existing functions to handle more complex dialogue patterns
4. Keep this log updated with daily progress and issues encountered
5. Explore alternative models if rate limits become an issue

### Conclusion

Today's work successfully migrated the course exercises from OpenAI to a free Hugging Face model. The key achievements were:
- Resolved environment variable loading by pointing to the correct .env path
- Implemented Hugging Face's OpenAI-compatible interface
- Standardized error handling and documentation across the codebase
- Created a sustainable approach for future learning without incurring API costs

These changes establish a good foundation for continuing Andrew Ng's AI coursework while building practical skills in working with open-source LLM APIs.