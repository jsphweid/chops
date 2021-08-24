import axiod from "https://deno.land/x/axiod@0.22/mod.ts";

import { Utils } from "../../utils.ts";
import { ParsedUserFile } from "../types.ts";

const user = JSON.parse(
  Deno.readTextFileSync("session.json")
) as ParsedUserFile;
const { sessionCSRF, sessionId } = user;

export const authHeaders = {
  "Content-Type": "application/json",
  "x-csrftoken": sessionCSRF,
  cookie: Utils.mapToCookie({
    csrftoken: sessionCSRF,
    LEETCODE_SESSION: sessionId,
  }),
};

export const client = axiod.create({
  baseURL: "https://leetcode.com",
  headers: authHeaders,
});
