import { useQuery } from "@tanstack/react-query";
import { getFeatures } from "@/api/auth";

/** Whether this server sends email; `undefined` while unknown. A failed probe counts as off. */
export function useMailFeature(): boolean | undefined {
  const { data, isError } = useQuery({ queryKey: ["auth", "features"], queryFn: getFeatures, staleTime: Infinity });
  return isError ? false : data?.mail;
}
