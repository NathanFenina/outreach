import { NextResponse } from "next/server";

// Auth de l'app. Deux modes, combinables :
//  1) MAGIC_TOKEN (recommandé mobile) : ouvre l'app une fois avec ?key=<MAGIC_TOKEN>
//     -> pose un cookie longue durée (180j) -> plus jamais de mot de passe.
//     Bookmark le lien sur l'écran d'accueil du téléphone = accès 1 tap.
//  2) BASIC_AUTH_USER / BASIC_AUTH_PASSWORD : Basic Auth classique (fallback desktop).
// Si aucune variable n'est définie, l'app reste ouverte (local).
export function middleware(req) {
  const user = process.env.BASIC_AUTH_USER;
  const pass = process.env.BASIC_AUTH_PASSWORD;
  const magic = process.env.MAGIC_TOKEN;

  // --- Mode 1 : magic link ---
  if (magic) {
    const url = req.nextUrl;
    // clic sur le lien magique -> pose le cookie, nettoie l'URL
    if (url.searchParams.get("key") === magic) {
      const clean = url.clone();
      clean.searchParams.delete("key");
      const res = NextResponse.redirect(clean);
      res.cookies.set("dcp_auth", magic, {
        httpOnly: true,
        secure: true,
        sameSite: "lax",
        path: "/",
        maxAge: 60 * 60 * 24 * 180,
      });
      return res;
    }
    // cookie valide -> ok
    if (req.cookies.get("dcp_auth")?.value === magic) return NextResponse.next();
  }

  // --- Mode 2 : Basic Auth (fallback) ---
  if (user && pass) {
    const header = req.headers.get("authorization");
    if (header) {
      const [scheme, encoded] = header.split(" ");
      if (scheme === "Basic" && encoded) {
        const decoded = atob(encoded);
        const i = decoded.indexOf(":");
        if (decoded.slice(0, i) === user && decoded.slice(i + 1) === pass)
          return NextResponse.next();
      }
    }
    return new NextResponse("Authentification requise", {
      status: 401,
      headers: { "WWW-Authenticate": 'Basic realm="Outbound Decupler"' },
    });
  }

  // magic défini mais pas authentifié, et pas de Basic Auth -> bloque proprement
  if (magic) {
    return new NextResponse(
      "Accès protégé — ouvre ton lien magique (…?key=…) pour te connecter.",
      { status: 401, headers: { "content-type": "text/plain; charset=utf-8" } }
    );
  }

  // rien de configuré -> ouvert (local)
  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon.ico).*)"],
};
