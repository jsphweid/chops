import { Difficulty } from "./difficulty.ts";
import { LeetcodeService } from "./leetcode-service/index.ts";
import { State } from "./state.ts";
import { Utils } from "./utils.ts";

export const addProblemsToState = async () => {
  const slugs = State.getUniqueSolutionSlugs();
  const problemSlugs = State.getUniqueProblemSlugs();

  for (const slug of slugs) {
    if (!problemSlugs.has(slug)) {
      const result = await LeetcodeService.getProblemBySlug(slug);
      if (result) {
        const { problemId, titleSlug, difficulty } = result;
        const difficultyRating = Difficulty.toIndex(
          Difficulty.fromString(difficulty)
        );
        if (difficultyRating < 0) {
          throw new Error(`Difficulty "${difficulty}" unrecognized...`);
        }
        State.upsertProblem({
          id: problemId,
          slug: titleSlug,
          difficulty: difficultyRating,
        });
      }
      await Utils.timeout(1000); // so we don't hit rate limit (I don't want to implement retries)
    }
  }
};
