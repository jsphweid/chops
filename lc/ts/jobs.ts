import { LeetcodeService } from "./leetcode-service/index.ts";
import { State } from "./state.ts";
import { Utils } from "./utils.ts";

export const addProblemsToState = async () => {
  const slugs = State.getUniqueSolutionSlugs();
  const problemSlugs = State.getUniqueProblemSlugs();

  for (const slug of slugs) {
    if (!problemSlugs.has(slug)) {
      const result = await LeetcodeService.getQuestionBySlug(slug);
      if (result) {
        const { questionId, titleSlug, difficulty } = result;
        const difficultyRating = ["Easy", "Medium", "Hard"].indexOf(difficulty);
        if (difficultyRating < 0) {
          throw new Error(`Difficulty "${difficulty}" unrecognized...`);
        }
        State.upsertProblem({
          id: questionId,
          slug: titleSlug,
          difficulty: difficultyRating as 0 | 1 | 2,
        });
      }
      await Utils.timeout(1000); // so we don't hit rate limit (I don't want to implement retries)
    }
  }
};
