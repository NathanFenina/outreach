import "./globals.css";

export const metadata = {
  title: "Décupler — Outbound",
  description: "Audiences & prospects cold mail / cold call",
};

export default function RootLayout({ children }) {
  return (
    <html lang="fr">
      <body>{children}</body>
    </html>
  );
}
