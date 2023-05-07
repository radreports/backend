dr = {
  "resourceType" : "DiagnosticReport",
 
  "text" : {
    "status" : "generated",
    "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h2><span title=\"Codes: {http://snomed.info/sct 429858000}\">CT of head-neck</span> (<span title=\"Codes: {http://snomed.info/sct 394914008}, {http://terminology.hl7.org/CodeSystem/v2-0074 RAD}\">Radiology</span>) </h2><table class=\"grid\"><tr><td>Subject</td><td><b>Roel(OFFICIAL)</b> male, DoB: 1960-03-13 ( BSN:\u00a0123456789\u00a0(use:\u00a0OFFICIAL))</td></tr><tr><td>When For</td><td>2012-12-01T12:00:00+01:00</td></tr><tr><td>Reported</td><td>2012-12-01T12:00:00+01:00</td></tr></table><p><b>Report Details</b></p><div><p>CT brains: large tumor sphenoid/clivus.</p>\n</div><p><b>Coded Conclusions :</b></p><ul><li><span title=\"Codes: {http://snomed.info/sct 188340000}\">Malignant tumor of craniopharyngeal duct</span></li></ul></div>"
  },
  "contained" : [{
    "resourceType" : "ImagingStudy",
    "id" : "74",
    "status" : "available",
    "subject" : {
      "reference" : "Patient/1"
    },
    "description" : "HEAD and NECK CT DICOM imaging study"
  }],
  "status" : "final",
  "category" : [{
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "394914008",
      "display" : "Radiology"
    },
    {
      "system" : "http://terminology.hl7.org/CodeSystem/v2-0074",
      "code" : "RAD"
    }]
  }],
  "code" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "429858000",
      "display" : "Computed tomography (CT) of head and neck"
    }],
    "text" : "CT of head-neck"
  },
  "subject" : {
    "reference" : "Patient/1",
    "display" : "Roel"
  },
  "effectiveDateTime" : "2012-12-01T12:00:00+01:00",
  "issued" : "2012-12-01T12:00:00+01:00",
  
  "conclusion" : "CT brains: large tumor sphenoid/clivus.",
  "conclusionCode" : [{
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "188340000",
      "display" : "Malignant tumor of craniopharyngeal duct"
    }]
  }]
}