import { createContext, useContext, useEffect, useState } from "react";
import { useRouter } from "next/router";

// Stores `routeNotFound` and `setRouteNotFound` state as top-level context.
export const ClientSideRoutingContext = createContext(null)

// Wrap the app in this provider to enable client-side routing via
// `useClientSideRouting` hook in a page component.
export function ClientSideRoutingProvider({ children }) {
  const [routeNotFound, setRouteNotFound] = useState(false);
  const [didRedirect, setDidRedirect] = useState(false);
  return (
    <ClientSideRoutingContext.Provider value={[routeNotFound, setRouteNotFound, setDidRedirect]}>
      {children}
    </ClientSideRoutingContext.Provider>
  )
}

// React hook for page components to redirect to the given URL when loading
// the 404 page. Also resets the `routeNotFound` state when navigating to a
// non-404 page.
export const useClientSideRouting = () => {
  const [routeNotFound, setRouteNotFound, setDidRedirect] = useContext(ClientSideRoutingContext)
  const router = useRouter()
  useEffect(() => {
    if (!routeNotFound) {
      if (router.pathname === "/404" && window.location.pathname !== router.pathname) {
        setDidRedirect(true)
        router.replace({
            pathname: window.location.pathname,
            query: window.location.search.slice(1),
        })
        .catch((e) => {
          setRouteNotFound(true)  // couldn't navigate, show 404
          setDidRedirect(false)
        })
      }
    } else if (router.pathname !== "/404") {
      setRouteNotFound(false)  // non-404 page, route _was_ found
    }
  }, []);
  useEffect(() => {
    const change_complete = () => {
      if (routeNotFound && router.pathname !== "/404") {
        setRouteNotFound(false)  // non-404 page, route _was_ found (via navigation)
      }
    }
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])
  return [routeNotFound, setDidRedirect]
}