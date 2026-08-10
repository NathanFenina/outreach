import Dashboard from "../../components/Dashboard";

export const dynamic = "force-dynamic";

export default function ColdMail({ searchParams }) {
  return <Dashboard channel="email" audienceId={searchParams?.audience || null} />;
}
