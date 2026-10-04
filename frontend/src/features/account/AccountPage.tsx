import { useState, type FormEvent } from "react";
import { useTranslation } from "react-i18next";
import type { Me } from "@/api/auth";
import { resendVerification } from "@/api/auth";
import { apiErrorMessage } from "@/api/client";
import { useAuth } from "@/auth/AuthContext";
import { useMailFeature } from "@/auth/useMailFeature";
import { Badge, Button, Card, Input, Label } from "@/components/ui/primitives";
import { showToast } from "@/lib/toastBus";

function EmailStatus({ user, mail }: { user: Me; mail: boolean | undefined }) {
  const { t } = useTranslation();
  const [busy, setBusy] = useState(false);

  if (!user.email) return <p className="text-sm text-gray-500 dark:text-gray-400">{t("account.emailNone")}</p>;
  if (user.email_verified) return <Badge tone="green">{t("account.emailVerified")}</Badge>;

  async function onResend() {
    setBusy(true);
    try {
      await resendVerification();
      showToast(t("account.verificationSent"), "success");
    } catch (err) {
      showToast(apiErrorMessage(err, t), "error");
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="space-y-2">
      <Badge tone="amber">{t("account.emailPending")}</Badge>
      {mail === false ? (
        <p className="text-sm text-gray-500 dark:text-gray-400">{t("account.mailUnavailable")}</p>
      ) : (
        <div className="flex flex-wrap items-center gap-2">
          <p className="text-sm text-gray-500 dark:text-gray-400">{t("account.checkInbox")}</p>
          <Button variant="secondary" disabled={busy || mail === undefined} onClick={() => void onResend()}>
            {t("account.resend")}
          </Button>
        </div>
      )}
    </div>
  );
}

function EmailForm({ user }: { user: Me }) {
  const { t } = useTranslation();
  const { setEmail } = useAuth();
  const [value, setValue] = useState(user.email ?? "");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const trimmed = value.trim();

  async function save(email: string | null) {
    setError(null);
    setBusy(true);
    try {
      await setEmail(email);
      showToast(t("common.saved"), "success");
    } catch (err) {
      setError(apiErrorMessage(err, t));
    } finally {
      setBusy(false);
    }
  }

  function onSubmit(e: FormEvent) {
    e.preventDefault();
    void save(trimmed || null);
  }

  return (
    <form onSubmit={onSubmit} className="space-y-2">
      <Label htmlFor="email">{t("auth.email")}</Label>
      <div className="flex flex-col gap-2 sm:flex-row">
        <Input id="email" type="email" autoComplete="email" value={value} invalid={error !== null} onChange={(e) => setValue(e.target.value)} />
        <Button type="submit" disabled={busy || trimmed.toLowerCase() === (user.email ?? "")}>
          {t("account.save")}
        </Button>
        {user.email && (
          <Button variant="ghost" disabled={busy} onClick={() => void save(null)}>
            {t("account.remove")}
          </Button>
        )}
      </div>
      <p className="text-xs text-gray-500 dark:text-gray-400">{t("account.emailHint")}</p>
      {error && <p className="text-sm text-red-600 dark:text-red-400">{error}</p>}
    </form>
  );
}

export function AccountPage() {
  const { t } = useTranslation();
  const { user } = useAuth();
  const mail = useMailFeature();
  if (!user) return null;

  return (
    <div className="mx-auto max-w-2xl space-y-4">
      <h1 className="text-2xl font-bold">{t("account.title")}</h1>
      <Card className="space-y-1 p-4">
        <p className="text-xs text-gray-500 dark:text-gray-400">{t("auth.username")}</p>
        <p className="font-semibold">{user.username}</p>
      </Card>
      <Card className="space-y-4 p-4">
        {/* Keyed on the saved address so the field resets when it changes elsewhere. */}
        <EmailForm key={user.email ?? ""} user={user} />
        <EmailStatus user={user} mail={mail} />
      </Card>
    </div>
  );
}
