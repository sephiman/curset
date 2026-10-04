import { apiClient } from "@/api/client";

export type Locale = "en" | "es";

export interface Me {
  id: string;
  username: string;
  locale: Locale;
  email: string | null;
  email_verified: boolean;
}

export async function getMe(): Promise<Me> {
  const { data } = await apiClient.get<Me>("/auth/me");
  return data;
}

export async function login(username: string, password: string): Promise<Me> {
  const { data } = await apiClient.post<Me>("/auth/login", { username, password });
  return data;
}

export async function register(
  username: string,
  password: string,
  locale: Locale,
  email: string | null,
  courses: string[],
): Promise<Me> {
  const { data } = await apiClient.post<Me>("/auth/register", { username, password, locale, email, courses });
  return data;
}

export async function logout(): Promise<void> {
  await apiClient.post("/auth/logout");
}

export async function updateLocale(locale: Locale): Promise<Me> {
  const { data } = await apiClient.patch<Me>("/auth/me", { locale });
  return data;
}

/** `null` removes the address; any change leaves it unverified until the mailed link is opened. */
export async function updateEmail(email: string | null): Promise<Me> {
  const { data } = await apiClient.patch<Me>("/auth/me", { email });
  return data;
}

export async function getFeatures(): Promise<{ mail: boolean }> {
  const { data } = await apiClient.get<{ mail: boolean }>("/auth/features");
  return data;
}

export async function resendVerification(): Promise<void> {
  await apiClient.post("/auth/email/verification");
}

export async function confirmVerification(token: string): Promise<void> {
  await apiClient.post("/auth/email/verification/confirm", { token });
}

export async function requestReset(email: string): Promise<void> {
  await apiClient.post("/auth/password-reset", { email });
}

export async function validateReset(token: string): Promise<void> {
  await apiClient.post("/auth/password-reset/validate", { token });
}

export async function confirmReset(token: string, newPassword: string): Promise<void> {
  await apiClient.post("/auth/password-reset/confirm", { token, new_password: newPassword });
}
