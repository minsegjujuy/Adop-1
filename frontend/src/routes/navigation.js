import React from "react";
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import { map } from "lodash";
import routes from "./routes";

export default function Navigation() {
  return (
    <div className="App">
      <Router>
        <Routes>
          {map(routes, (route, index) => (
            <Route
              key={index}
              path={route.path}
              element={
                <route.layout>
                  <route.component />
                </route.layout>
              }
            />
          ))}
        </Routes>
      </Router>
    </div>
  );
}