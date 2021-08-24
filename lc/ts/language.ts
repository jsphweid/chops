export namespace Language {
  export const PYTHON = "PYTHON";
  export const values = [PYTHON] as const;
  export type Type = typeof values[number];

  export const fromCliArgs = (strings: string[]): Type | null =>
    // TODO: how are the types _this_ messy
    strings.find((str) =>
      values.includes(str.toUpperCase() as any)
    ) as Type | null;

  export const toLeetcodeSlugName = (val: Type): string =>
    ({
      [PYTHON]: "python3",
    }[val]);

  export const getFileExtension = (val: Type) =>
    ({
      [PYTHON]: "py",
    }[val]);
}
