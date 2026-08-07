import { NextResponse } from "next/server";

// Protection Basic Auth de toute l'app.
// Définis BASIC_AUTH_USER et BASIC_AUTH_PASSWORD dans Vercel pour l'activer.
// Sans ces variables, l'app reste ouverte (utile en local).
export function middleware(req) {
  const user = process.env.BASIC_AUTH_USER;
  const pass = process.env.BASIC_AUTH_PASSWORD;
  if (!user || !pass) return NextResponse.next();

  const header = req.headers.get("authorization");
  if (header) {
    const [scheme, encoded] = header.split(" ");
    if (scheme === "Basic" && encoded) {
      const decoded = atob(encoded);
      const i = decoded.indexOf(":");
      const u = decoded.slice(0, i);
      const p = decoded.slice(i + 1);
      if (u === user && p === pass) return NextResponse.next();
    }
  }
  return new NextResponse("Authentification requise", {
    status: 401,
    headers: { "WWW-Authenticate": 'Basic realm="Outbound Decupler"' },
  });
}

export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon.ico).*)"],
};
