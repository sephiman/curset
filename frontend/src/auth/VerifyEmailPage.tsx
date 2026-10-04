import { useEffect, useRef, useState } from "react";
import { Link, useSearchParams } from "react-router-dom";
import { useTranslation } from "react-i18next";
import { confirmVerification } from "@/api/auth";
import { apiErrorMessage } from "@/api/client";
import { useAuth } from "@/auth/AuthContext";
import { AuthCard } from "@/auth/AuthCard";

type Outcome = { state: "pending" } | { state: "done" } | { state: "failed"; message: string };

export function VerifyEmailPage() {
  const { t } = useTranslation();
  const { user, refresh } = useAuth();
  const token = useSearchParams()[0].get("token") ?? "";
  const [outcome, setOutcome] = useState<Outcome>({ state: "pending" });
  // The link is single-use: StrictMode's second effect run would spend it and report a failure.
  const sent = useRef(false);

  useEffect(() => {
    if (sent.current) return;
    sent.current = true;
    if (!token) {
      setOutcome({ state: "failed", message: t("errors.VERIFY_TOKEN_INVALID") });
      return;
    }
    confirmVerification(token)
      .then(async () => {
        setOutcome({ state: "done" });
        await refresh();
      })
      .catch((err: unknown) => setOutcome({ state: "failed", message: apiErrorMessage(err, t) }));
  }, [token, t, refresh]);

  return (
    <AuthCard title={t("auth.verifyTitle")}>
      <div className="space-y-4 text-center text-sm">
        {outcome.state === "pending" && <p className="text-gray-500 dark:text-gray-400">{t("common.loading")}</p>}
        {outcome.state === "done" && <p className="text-gray-700 dark:text-gray-200">{t("auth.verifyDone")}</p>}
        {outcome.state === "failed" && <p className="text-red-600 dark:text-red-400">{outcome.message}</p>}
        <Link to={user ? "/account" : "/login"} className="block font-medium text-primary hover:underline">
          {user ? t("account.title") : t("auth.backToLogin")}
        </Link>
      </div>
    </AuthCard>
  );
}
