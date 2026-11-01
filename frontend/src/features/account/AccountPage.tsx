import { useState, type FormEvent } from "react";
import { useTranslation } from "react-i18next";
import type { Me } from "@/api/auth";
import { changePassword, resendVerification } from "@/api/auth";
import { apiErrorMessage } from "@/api/client";
import { useAuth } from "@/auth/AuthContext";
import { useMailFeature } from "@/auth/useMailFeature";
import { Badge, Button, Card, Input, Label } from "@/components/ui/primitives";
import { showToast } from "@/lib/toastBus";
import { CourseSettings } from "@/features/courses/CourseSettings";

function EmailStatus({ user, mail }: { user: Me; mail: boolean | undefined }) {
  const { t } = useTranslation();
  const [busy, setBusy] = useState(false);

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

function NameForm({ user }: { user: Me }) {
  const { t } = useTranslation();
  const { setName } = useAuth();
  const [value, setValue] = useState(user.name ?? "");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const trimmed = value.trim();

  async function save(name: string | null) {
    setError(null);
    setBusy(true);
    try {
      await setName(name);
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
      <Label htmlFor="name">{t("account.name")}</Label>
      <div className="flex flex-col gap-2 sm:flex-row">
        <Input
          id="name"
          type="text"
          autoComplete="name"
          maxLength={100}
          value={value}
          invalid={error !== null}
          onChange={(e) => setValue(e.target.value)}
        />
        <Button type="submit" disabled={busy || trimmed === (user.name ?? "")}>
          {t("account.save")}
        </Button>
        {user.name && (
          <Button variant="ghost" disabled={busy} onClick={() => void save(null)}>
            {t("account.remove")}
          </Button>
        )}
      </div>
      <p className="text-xs text-gray-500 dark:text-gray-400">{t("account.nameHint")}</p>
      {error && <p className="text-sm text-red-600 dark:text-red-400">{error}</p>}
    </form>
  );
}

function EmailForm({ user }: { user: Me }) {
  const { t } = useTranslation();
  const { setEmail } = useAuth();
  const [value, setValue] = useState(user.email);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const trimmed = value.trim().toLowerCase();

  async function save(email: string) {
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
    if (!trimmed) return;
    void save(trimmed);
  }

  return (
    <form onSubmit={onSubmit} className="space-y-2">
      <Label htmlFor="email">{t("auth.email")}</Label>
      <div className="flex flex-col gap-2 sm:flex-row">
        <Input
          id="email"
          type="email"
          autoComplete="email"
          required
          value={value}
          invalid={error !== null}
          onChange={(e) => setValue(e.target.value)}
        />
        <Button type="submit" disabled={busy || trimmed === user.email.toLowerCase()}>
          {t("account.save")}
        </Button>
      </div>
      <p className="text-xs text-gray-500 dark:text-gray-400">{t("account.emailHint")}</p>
      {error && <p className="text-sm text-red-600 dark:text-red-400">{error}</p>}
    </form>
  );
}

function PasswordForm() {
  const { t } = useTranslation();
  const [currentPassword, setCurrentPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    if (newPassword.length < 8) {
      setError(t("auth.passwordTooShort", { count: 8 }));
      return;
    }
    if (newPassword !== confirmPassword) {
      setError(t("account.passwordsDiffer"));
      return;
    }
    setBusy(true);
    try {
      await changePassword(currentPassword, newPassword);
      setCurrentPassword("");
      setNewPassword("");
      setConfirmPassword("");
      showToast(t("account.passwordChanged"), "success");
    } catch (err) {
      setError(apiErrorMessage(err, t));
    } finally {
      setBusy(false);
    }
  }

  return (
    <form onSubmit={onSubmit} className="space-y-3">
      <h2 className="text-base font-semibold">{t("account.changePassword")}</h2>
      <div>
        <Label htmlFor="current-password">{t("account.currentPassword")}</Label>
        <Input
          id="current-password"
          type="password"
          autoComplete="current-password"
          required
          value={currentPassword}
          onChange={(e) => setCurrentPassword(e.target.value)}
        />
      </div>
      <div>
        <Label htmlFor="new-password">{t("account.newPassword")}</Label>
        <Input
          id="new-password"
          type="password"
          autoComplete="new-password"
          required
          minLength={8}
          value={newPassword}
          onChange={(e) => setNewPassword(e.target.value)}
        />
        <p className="mt-1 text-xs text-gray-500 dark:text-gray-400">{t("auth.passwordHint", { count: 8 })}</p>
      </div>
      <div>
        <Label htmlFor="confirm-password">{t("account.repeatNewPassword")}</Label>
        <Input
          id="confirm-password"
          type="password"
          autoComplete="new-password"
          required
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
        />
      </div>
      {error && <p className="text-sm text-red-600 dark:text-red-400">{error}</p>}
      <Button type="submit" disabled={busy || !currentPassword || !newPassword || !confirmPassword}>
        {busy ? t("common.loading") : t("account.savePassword")}
      </Button>
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
      <Card className="space-y-4 p-4">
        <NameForm key={user.name ?? ""} user={user} />
      </Card>
      <Card className="space-y-4 p-4">
        <EmailForm key={user.email} user={user} />
        <EmailStatus user={user} mail={mail} />
      </Card>
      <Card className="p-4">
        <PasswordForm />
      </Card>
      <CourseSettings />
    </div>
  );
}
