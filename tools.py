def generate_test_scenarios(feature_description: str) -> str:
    prompt = f"""
You are a senior QA engineer.

Generate comprehensive test scenarios for the feature below.

Feature:
{feature_description}

Include:

1. Positive test cases
2. Negative test cases
3. Edge cases
4. Security scenarios
5. Boundary value cases

Return the output in a clear numbered list.
"""
    return prompt