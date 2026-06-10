from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """
    ESSENTIAL: This tool MUST be used strictly for solving mathematical calculations and obtaining exact results.
    Do not use this tool for general knowledge questions.
    The input must be a simple and valid mathematical expression in Python (example: '128 * 46', '10 / 2', '5 + 5').
    """
    try:
        # Restricted assessment for basic safety in testing.
        result = eval(expression, {"__builtins__": None}, {})
        return str(result)
    except Exception as e:
        return f"Error in calculation execution: {e}"