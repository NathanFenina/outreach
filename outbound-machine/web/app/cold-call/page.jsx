import Dashboard from "../../components/Dashboard";

export const dynamic = "force-dynamic";

export default function ColdCall({ searchParams }) {
  return <Dashboard channel="call" audienceId={searchParams?.audience || null} />;
}
