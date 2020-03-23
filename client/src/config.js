let config;

if (process.env.NODE_ENV === "production") {
  config = {
    API_BASE: "https://rocplannerapi.appspot.com/api",
  };
} else {
  config = {
    API_BASE: "http://localhost:5000/api",
  };
}

export { config }
