// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import "./App.css";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

import Layout from "./Layout/Layout";
import Login from "./pages/Login";
import Profile from "./pages/Profile";
import Filter from "./pages/Filter";

// import { GoogleLogin } from '@react-oauth/google';

const router = createBrowserRouter([
  {
    path: "/",
    element: (
      <>
        <Layout />
      </>
    ),
    children: [
      {
        path: "/",
        element: <Login />,
      },
      {
        path: "/Profile",
        element: <Profile />,
      },
      {
        path: "/Filter",
        element: <Filter />,
      },
    ],
  },
]);

function App() {
  return (
    <div>
      <RouterProvider router={router} />
    </div>
  );
}

export default App;
