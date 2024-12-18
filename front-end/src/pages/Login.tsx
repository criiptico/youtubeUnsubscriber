import { useGoogleLogin } from "@react-oauth/google";
import { useState } from "react";

function Login() {
  const [signingIn, setSigningIn] = useState(false);
  const [access, setAccess] = useState(false);
  // const [errorDetected, setErrorDetected] = useState(false);

  function auth_user(auth_obj) {
    const update = {
      title: "Authentication Code",
      code: auth_obj.code,
    };

    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/JSON",
        "Access-Control-Request-Method": "POST",
        "Access-Control-Request-Headers": "content-type,x-pingother",
      },
      body: JSON.stringify(update),
    };

    const response = fetch("http://localhost:5000/userLogin/", options)
      .then((http_response) => {
        // console.log(http_response);
        return http_response.json();
      })
      .then((data) => {
        console.log("Success:");
        console.log(data);

        return data;
      })
      .catch((error) => {
        console.error("Error:", error);
      });

    return true;
  }

  function GoogleLoginEventHandler() {
    setSigningIn(true);
    login();
  }

  const login = useGoogleLogin({
    onSuccess: (codeResponse) => {
      console.log("On success response: ");
      console.log(codeResponse);
      setAccess(auth_user(codeResponse));
    },
    onError: (response) => {
      console.log("Error google login.");
      console.log(response);
      throw new Error("Error google login.");
    },
    flow: "auth-code",
    scope: [
      "https://www.googleapis.com/auth/youtube.readonly",
      "https://www.googleapis.com/auth/youtube",
      "https://www.googleapis.com/auth/youtube.force-ssl",
    ].join(" "),
  });

  // "email profile https://www.googleapis.com/auth/youtube.readonly https://www.googleapis.com/auth/youtube https://www.googleapis.com/auth/youtube.force-ssl openid https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"

  // Send token response to server
  // Server is run with python as the back end on firebase
  // Loading wheel scene
  // Redirect to Profile scene when server responds
  // Profile scene displays the channel's that they're subscribed to

  // async function user_login(auth_code){
  //     // The auth_code is sent to the backend and the backend handles the access code, refresh code, and database management
  //     const backend_url = "localhost:";
  // }

  return (
    <div className="App">
      <header className="App-header">
        <h1>Filter YouTube Subscriptions</h1>
        <p>Sign in with Google to use this app.</p>

        <div>
          <button onClick={() => GoogleLoginEventHandler()}>
            Sign in with Google 🚀
          </button>
          {signingIn && access ? (
            <div>Signed In.</div>
          ) : signingIn ? (
            <div>Signing In.</div>
          ) : (
            <div>Must Sign In.</div>
          )}
        </div>
      </header>
    </div>
  );
}

export default Login;
