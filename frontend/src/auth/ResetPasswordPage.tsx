import { useEffect, useState, type FormEvent } from "react";
import { Link, useNavigate, useSearchParams } from "react-router-dom";
import { useTranslation } from "react-i18next";
import { confirmReset, validateReset } from "@/api/auth";
import { apiErrorMessage } from "@/api/client";
import { AuthCard } from "@/auth/AuthCard";
import { Button, Input, Label } from "@/components/ui/primitives";
import { showToast } from "@/lib/toastBus";

const MIN_PASSWORD = 8;

export function ResetPasswordPage() {
  const { t } = useTranslation();
  const navigate = useNavigate();
  const token = useSearchParams()[0].get("token") ?? "";
  const [invalid, setInvalid] = useState<string | null>(null);
  const [password, setPassword] = useState("");
  const [confirm, setConfirm] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    if (!token) {
      setInvalid(t("errors.RESET_TOKEN_INVALID"));
      return;
    }
    validateReset(token).catch((err: unknown) => setInvalid(apiErrorMessage(err, t)));
  }, [token, t]);

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    if (password !== confirm) {
      setError(t("auth.passwordsDiffer"));
      return;
    }
    setBusy(true);
    setError(null);
    try {
      await confirmReset(token, password);
      showToast(t("auth.resetDone"), "success", 6000);
      navigate("/login", { replace: true });
    } catch (err) {
      setError(apiErrorMessage(err, t));
    } finally {
      setBusy(false);
    }
  }

  return (
    <AuthCard title={t("auth.resetTitle")}>
      {invalid ? (
        <div className="space-y-4 text-center text-sm">
          <p className="text-red-600 dark:text-red-400">{invalid}</p>
          <Link to="/forgot-password" className="font-medium text-primary hover:underline">
            {t("auth.requestAnother")}
          </Link>
        </div>
      ) : (
        <form onSubmit={onSubmit} className="space-y-4">
          <div>
            <Label htmlFor="password">{t("auth.newPassword")}</Label>
            <Input id="password" type="password" autoComplete="new-password" required minLength={MIN_PASSWORD} value={password} onChange={(e) => setPassword(e.target.value)} />
            <p className="mt-1 text-xs text-gray-500 dark:text-gray-400">{t("auth.passwordHint", { count: MIN_PASSWORD })}</p>
          </div>
          <div>
            <Label htmlFor="confirm">{t("auth.confirmPassword")}</Label>
            <Input id="confirm" type="password" autoComplete="new-password" required value={confirm} onChange={(e) => setConfirm(e.target.value)} />
          </div>
          {error && <p className="text-sm text-red-600 dark:text-red-400">{error}</p>}
          <Button type="submit" disabled={busy} className="w-full">
            {busy ? t("common.loading") : t("auth.setPassword")}
          </Button>
        </form>
      )}
    </AuthCard>
  );
}
