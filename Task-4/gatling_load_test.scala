import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class LoadTestSimulation extends Simulation {

  // Define the HTTP protocol
  val httpProtocol = http
    .baseUrl("http://localhost:3000") // Replace with your application's URL
    .acceptHeader("application/json")

  // Define the scenario
  val scn = scenario("Load Test Scenario")
    .exec(http("Submit Form")
      .post("/submit") // Replace with your form submission endpoint
      .formParam("inputField", "test input") // Adjust as necessary
      .check(status.is(200)))

  // Set up the load test
  setUp(
    scn.inject(
      atOnceUsers(100), // Adjust the number of users as needed
      rampUsers(500) during (10.minutes) // Gradually increase users
    )
  ).protocols(httpProtocol)
}
