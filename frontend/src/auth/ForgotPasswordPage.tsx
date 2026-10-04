import { useState, type FormEvent } from "react";
import { Link } from "react-router-dom";
import { useTranslation } from "react-i18next";
import { requestReset } from "@/api/auth";
import { apiErrorMessage } from "@/api/client";
import { AuthCard } from "@/auth/AuthCard";
import { useMailFeature } from "@/auth/useMailFeature";
import { Button, Input, Label } from "@/components/ui/primitives";

export function ForgotPasswordPage() {
  const { t } = useTranslation();
  const mail = useMailFeature();
  const [email, setEmail] = useState("");
  const [sent, setSent] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setBusy(true);
    try {
      await requestReset(email);
      setSent(true);
    } catch (err) {
      setError(apiErrorMessage(err, t));
    } finally {
      setBusy(false);
    }
  }

  return (
    <AuthCard title={t("auth.forgotTitle")}>
      {mail === false ? (
        <p className="text-sm text-gray-600 dark:text-gray-300">{t("auth.resetUnavailable")}</p>
      ) : sent ? (
        <p className="text-sm text-gray-600 dark:text-gray-300">{t("auth.resetSent")}</p>
      ) : (
        <form onSubmit={onSubmit} className="space-y-4">
          <p className="text-sm text-gray-600 dark:text-gray-300">{t("auth.forgotIntro")}</p>
          <div>
            <Label htmlFor="email">{t("auth.email")}</Label>
            <Input id="email" type="email" autoComplete="email" required value={email} onChange={(e) => setEmail(e.target.value)} />
          </div>
          {error && <p className="text-sm text-red-600 dark:text-red-400">{error}</p>}
          <Button type="submit" disabled={busy || mail === undefined} className="w-full">
            {busy ? t("common.loading") : t("auth.sendResetLink")}
          </Button>
        </form>
      )}
      <p className="mt-4 text-center text-sm">
        <Link to="/login" className="font-medium text-primary hover:underline">
          {t("auth.backToLogin")}
        </Link>
      </p>
    </AuthCard>
  );
}
