ep = {
  "resourceType" : "Endpoint",
  "id" : "1558",
  "text" : {
    "status" : "generated",
    "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\">\n\t\t\tHealth Intersections CarePlan Hub<br/>\n\t\t\tCarePlans can be uploaded to/from this loccation\n\t\t</div>"
  },
  "identifier" : [{
    "system" : "http://pacs.radreports.ai",
    "value" : "epcp12"
  }],
  "status" : "active",
  "connectionType" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/endpoint-connection-type",
      "code" : "hl7-fhir-rest"
    }]
  }],
  "name" : "Health Intersections CarePlan Hub",
  "description" : "The CarePlan hub provides a test/dev environment for testing submissions",
  "environmentType" : [{
    "coding" : [{
      "system" : "http://hl7.org/fhir/endpoint-environment",
      "code" : "test"
    }]
  },
  {
    "coding" : [{
      "system" : "http://hl7.org/fhir/endpoint-environment",
      "code" : "dev"
    }]
  }],"address" : "http://fhir3.healthintersections.com.au/open/CarePlan",
  "header" : ["bearer-code BASGS534s4"]
}