import { format } from "https://deno.land/std@0.91.0/datetime/mod.ts";

import { Language } from "./language.ts";

export namespace Utils {
  const TIMESTAMP_FORMAT = "yyyy.MM.dd-HH.mm.ss";
  export const timeout = (milliseconds: number): Promise<void> =>
    new Promise((resolve) => setTimeout(() => resolve(), milliseconds));

  export const mapToCookie = (map: { [key: string]: string }): string =>
    Object.entries(map).reduce(
      (previous, [key, value]) => `${previous} ${key}=${value};`,
      ""
    );

  export const newFilename = (language: Language.Type): string =>
    `${format(new Date(), TIMESTAMP_FORMAT)}.${Language.getFileExtension(
      language
    )}`;

  export const fromCliArgs = <T>(
    mapping: { [key: string]: T },
    strings: string[]
  ): T | null => {
    const filtered = strings.filter((str) =>
      Object.keys(mapping).includes(str)
    );
    if (filtered.length === 0) {
      return null;
    } else if (filtered.length > 1) {
      throw new Error(
        `Can not parse difficulty from strings. You must choose one between ${filtered}`
      );
    } else {
      return mapping[filtered[0] as keyof typeof mapping];
    }
  };

  export const exists = (str?: string): boolean => !!str;

  export const runCommand = async (command: string[]): Promise<void> => {
    // mostly copied from https://deno.land/manual@v1.12.2/examples/subprocess
    const p = Deno.run({
      cmd: command,
      stdout: "piped",
      stderr: "piped",
    });
    const { code } = await p.status();
    const rawOutput = await p.output();
    const rawError = await p.stderrOutput();
    if (code === 0) {
      await Deno.stdout.write(rawOutput);
    } else {
      const errorString = new TextDecoder().decode(rawError);
      console.log(errorString);
    }
  };

  export const printHTML = async (html: string): Promise<void> => {
    const tempFile = "temp.html";
    Deno.writeTextFileSync(tempFile, html);
    await runCommand(["python3", "html2text.py", tempFile]);
    Deno.removeSync(tempFile);
  };

  export const clearConsole = (): void => {
    // For some reason this seems necessary to get a good wipe
    console.clear();
    console.clear();
    console.clear();
    console.clear();
    console.clear();
    console.clear();
  };

  export const getEnumKeyByEnumValue = <T extends { [index: string]: string }>(
    myEnum: T,
    enumValue: string
  ): keyof T | null => {
    let keys = Object.keys(myEnum).filter((x) => myEnum[x] == enumValue);
    return keys.length > 0 ? keys[0] : null;
  };

  export const formatDate = (date: Date): string => {
    const year = date.getFullYear();

    let month = (1 + date.getMonth()).toString();
    month = month.length > 1 ? month : "0" + month;

    let day = date.getDate().toString();
    day = day.length > 1 ? day : "0" + day;

    return year + "-" + month + "-" + day;
  };

  export const addDays = (date: Date, daysToAdd: number): Date => {
    const newDate = new Date(date.valueOf());
    newDate.setDate(newDate.getDate() + daysToAdd);
    return newDate;
  };

  export const getDiffDays = (date1: Date, date2: Date) => {
    const diffTime = Math.abs(date2.getTime() - date1.getTime());
    return Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  };
}
