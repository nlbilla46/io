
export function onRequest(context) {
  const country = context.request.cf?.country || "XX";
  const premium = ["US", "CA", "AU", "GB", "DE", "FR"];

  if (premium.includes(country)) {
    return Response.redirect(new URL("/premium.html", context.request.url));
  }

  return context.next();
}
