import Ask from "https://deno.land/x/ask@1.0.6/mod.ts";
import * as FS from "https://deno.land/std@0.105.0/fs/mod.ts";
import * as Path from "https://deno.land/std@0.105.0/path/mod.ts";

import {
  getQuestionStartingCode,
  LeetcodeService,
} from "./leetcode-service/index.ts";
import { Language } from "./language.ts";
import { State } from "./state.ts";
import { Difficulty } from "./difficulty.ts";
import { SuggestedQuestion, Submission } from "./leetcode-service/types.ts";
import { Utils } from "./utils.ts";
import { Editor } from "./editor.ts";
import { enhanceStartingCode } from "./leetcode-service/code.ts";

const ask = new Ask();

const printFormattedQuestions = (questions: SuggestedQuestion.Type[]): void => {
  console.log("New Questions");
  for (const question of questions) {
    const link = `https://leetcode.com/problems/${question.titleSlug}/`;
    const comps = [
      question.titleSlug,
      question.title,
      link,
      question.difficulty,
    ];
    console.log(comps.join(" - "));
  }
  console.log("");
};

const printRedos = (redos: State.Redo[]): void => {
  console.log("Redos");
  redos.forEach((redo) => {
    console.log(
      `${redo.slug} - ${redo.representation} - ${redo.daysSinceLast} day(s) since last`
    );
  });
  console.log("");
};

const commands = {
  new: async (args: string[]) => {
    const language = Language.fromCliArgs(args) || Language.PYTHON;
    const difficulty = Difficulty.fromCliArgs(args) || Difficulty.choose();
    const questions = await LeetcodeService.getSuggestedQuestions(difficulty);
    printRedos(State.getRedos().slice(0, 5));
    printFormattedQuestions(questions);
    const { slug } = await ask.input({ name: "slug", validate: Utils.exists });
    const question = await LeetcodeService.getQuestionBySlug(slug as string);
    if (!question) {
      console.error("Slug you entered isn't tied to an actual question.");
      Deno.exit();
    }
    const baseDir = `answers/${slug as string}`;
    FS.ensureDirSync(baseDir);
    const startingCode = getQuestionStartingCode(question, language);
    const relativePath = `${baseDir}/${Utils.newFilename(language)}`;
    Deno.writeTextFileSync(relativePath, enhanceStartingCode(startingCode));
    const absolutePath = Path.resolve(relativePath);
    Utils.clearConsole();
    await Utils.printHTML(question.content);
    const link = `https://leetcode.com/problems/${slug}/`;
    console.log("*******Problem is printed above or see link:", link);
    const start = State.startNewSolution(
      question.questionId,
      slug as string,
      language,
      relativePath
    );
    console.log("*******Time starts now,", start.toLocaleString());
    console.log("*******File is available here ->", absolutePath);
    await Editor.openInRandomTextEditor(absolutePath);
    const submitCommand = `./lc.sh submit ${relativePath}`;
    console.log("*******Run this when ready to submit ->", submitCommand);
  },
  submit: async (args: string[]) => {
    if (args.length !== 1) {
      throw new Error("Too many args for `submit`");
    }
    const filepath = args[0];
    const solutionDetails = State.getSolutionDetails(filepath);
    if (!solutionDetails) {
      console.error("Couldn't find the solution locally:", filepath);
      Deno.exit();
    }
    console.log("Submitting...");
    const result = await LeetcodeService.submitAnswer({
      code: Deno.readTextFileSync(filepath),
      slug: solutionDetails.leetcodeSlug,
      questionId: solutionDetails.leetcodeId,
      language: solutionDetails.language,
    });
    if (Submission.isAccepted(result)) {
      State.registerSubmission(filepath, {
        date: new Date().toISOString(),
        leetcodeSubmissionId: result.submissionId,
        type: State.SubmissionType.SuccessfulSubmission,
      });
      console.log("Submission Succeeded!!!");
    } else {
      const submissionLink = `https://leetcode.com/submissions/detail/${result.submissionId}/`;
      console.log(`Submission failed... More details here: ${submissionLink}`);
      const { why } = await ask.input({ name: "why", validate: Utils.exists });
      State.registerSubmission(filepath, {
        failureReason: why,
        date: new Date().toISOString(),
        leetcodeSubmissionId: result.submissionId,
        type: State.SubmissionType.FailedSubmission,
      });
    }
  },
  report: (args: string[]) => {
    console.log(
      "Minutes to first solve (avg):",
      State.getAverageSecondsToFirstSolve() / 60
    );
    console.log("Unsolved problems:", State.getUnsolvedProblems());
  },
};

if (Deno.args.includes("--help")) {
  console.log("TODO: put help blurb here");
  Deno.exit();
}

if (Deno.args.length === 0 || !Object.keys(commands).includes(Deno.args[0])) {
  console.error(
    "Need args like 'new', 'submit', 'report'... \n" +
      "try --help for more info"
  );
  Deno.exit();
}

commands[Deno.args[0] as keyof typeof commands](Deno.args.slice(1));
