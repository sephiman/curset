import { request, type FullConfig } from "@playwright/test";
import { AEAT, AGE, AGE_C2, CRYPTO, STATE_FILE, USER } from "./session";

/** Signs in once per run (login is rate limited) and leaves the session cookie for every test. */
export default async function globalSetup(config: FullConfig): Promise<void> {
  const baseURL = config.projects[0].use.baseURL;
  const api = await request.newContext({ baseURL });
  let login = await api.post("/api/auth/login", { data: USER });
  if (!login.ok()) {
    const register = await api.post("/api/auth/register", {
      data: { ...USER, locale: "es", name: "e2e-mobile", courses: [AGE, CRYPTO, AGE_C2, AEAT] },
    });
    if (!register.ok()) throw new Error(`cannot register ${USER.email}: ${await register.text()}`);
    login = await api.post("/api/auth/login", { data: USER });
  }
  if (!login.ok()) throw new Error(`cannot sign in ${USER.email}: ${await login.text()}`);
  await api.storageState({ path: STATE_FILE });
  await api.dispose();
}
