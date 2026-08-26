import Dashboard from "../../components/Dashboard";

export const dynamic = "force-dynamic";
export const fetchCache = "force-no-store";
export const revalidate = 0;

export default function ColdMail({ searchParams }) {
  return <Dashboard channel="email" audienceId={searchParams?.audience || null} />;
}
