"use client";
import { usePathname } from "next/navigation";
import Link from "next/link";

export default function Tabs() {
  const path = usePathname();
  const items = [
    { href: "/cold-mail", label: "Cold Mail" },
    { href: "/cold-call", label: "Cold Call" },
  ];
  return (
    <nav className="tabs">
      {items.map((it) => (
        <Link
          key={it.href}
          href={it.href}
          className={"tab" + (path === it.href ? " active" : "")}
        >
          {it.label}
        </Link>
      ))}
    </nav>
  );
}
