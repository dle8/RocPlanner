let config;

if (process.env.NODE_ENV === "production") {
  config = {
    API_BASE: "https://uplanner.bopa.ng/api",
  };
} else {
  config = {
    API_BASE: "https://rocplanning.herokuapp.com/api",
  };
}

export { config }
