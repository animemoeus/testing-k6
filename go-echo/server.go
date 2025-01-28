package main

import (
	"net/http"

	"github.com/labstack/echo/v4"
)

func index(c echo.Context) error {
	return c.String(http.StatusOK, "Shinomiyaa ( •̀ ω •́ )✧")
}

func main() {
	e := echo.New()

	// Middleware
	// e.Use(middleware.Logger())

	e.GET("/", index)

	e.Logger.Fatal(e.Start(":8012"))
}
