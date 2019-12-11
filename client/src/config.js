let config;

if (process.env.NODE_ENV === "production") {
  config = {
    API_BASE: "",
  };
} else {
  config = {
    // API_BASE: "http://localhost:5000/api",
    API_BASE: "https://rocplanning.herokuapp.com/api",
  };
}

export { config }
