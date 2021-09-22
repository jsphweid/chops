import { Language } from "../language.ts";

const enhancePythonStartingCode = (code: string) => {
  return `
"""
===== Initial Thoughts =====


=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

${code}`;
};

export const enhanceStartingCode = (
  code: string,
  lang: Language.Type = Language.PYTHON
) => {
  /**
   * The start code template from LeetCode is extremely predictable
   * It's safe to add comment regions to the top but the bottom is trickier
   *
   */
  if (lang === Language.PYTHON) {
    return enhancePythonStartingCode(code);
  } else {
    throw new Error("Only Python is supported for enhancing starting code...");
  }
};
