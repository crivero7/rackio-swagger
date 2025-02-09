# -*- coding: utf-8 -*-
"""rackio_swagger/spec.py

This module implements the Rackio Swagger spec variable.
"""

swagger = {
    "swagger": "2.0",
    "basePath": "/api",
    "paths": {
        "/login": {
            "post": {
                "responses": {
                    "200": {
                        "description": "Success"
                    }
                },
                "parameters": [
                    {
                        "name": "payload",
                        "required": True,
                        "in": "body",
                        "schema": {
                            "$ref": "#/definitions/login_model"
                        }
                    }
                ],
                "tags": [
                    "auth"
                ]
            }
        },
        "/logout": {
            "get": {
                "responses": {
                    "200": {
                        "description": "Success"
                    }
                },
                "security": [
                    {
                        "apikey": []
                    }
                ],
                "tags": [
                    "auth"
                ]
            }
        },
        "/users": {
            "get": {
                "responses": {
                    200: {
                        "description": "Success"
                    }
                },
                "tags": ["users"]
            }
        },
        "/users/columns": {
            "get": {
                "responses": {
                    200: {
                        "description": "Success"
                    }
                },
                "tags": ["users"]
            }
        },
        "/users/columns/{column_name}": {
            "post": {
                "responses": {
                    200: {
                        "description": "Success"
                    }
                },
                "parameters": [
                    {
                        "name": "column_name",
                        "required": True,
                        "in": "path",
                        "type": "string"
                    },
                    {
                        "name": "payload",
                        "required": True,
                        "in": "body",
                        "schema": {
                            "$ref": "#/definitions/user_column_model"
                        }
                    }
                ],
                "tags": ["users"]
            }
        },
        "/users/license": {
            "post": {
                "responses": {
                    200: {
                        "description": "Success"
                    }
                },
                "parameters": [
                    {
                        "name": "payload",
                        "required": True,
                        "in": "body",
                        "schema": {
                            "$ref": "#/definitions/user_license_model"
                        }
                    }
                ],
                "tags": ["users"]
            }
        },
        "/license": {
            "post": {
                "responses": {
                    200: {
                        "description": "Success"
                    }
                },
                "parameters": [
                    {
                        "name": "payload",
                        "required": True,
                        "in": "body",
                        "schema": {
                            "$ref": "#/definitions/license_model"
                        }
                    }
                ],
                "tags": ["users"]
            }
        },
        "/tags": {
            "get": {
                "responses": {
                    200: {
                        "description": "Success"
                    }
                },
                "security": [
                    {
                        "apikey": []
                    }
                ],
                "tags": ["tags"]
            }
        },
        "/tags/{tag_id}": {
            "get": {
                "responses": {
                    200: {
                        "description": "Success"
                    }
                },
                "parameters": [
                    {
                        "name": "tag_id",
                        "required": True,
                        "in": "path",
                        "type": "string"
                    }
                ],
                "security": [
                    {
                        "apikey": []
                    }
                ],
                "tags": ["tags"] 
            },
            "post": {
                "responses": {
                        200: {
                            "description": "Success"
                        }
                    },
                "parameters": [
                    {
                        "name": "tag_id",
                        "required": True,
                        "in": "path",
                        "type": "string"
                    },
                    {
                        "name": "payload",
                        "required": True,
                        "in": "body",
                        "schema": {
                            "$ref": "#/definitions/tag_model"
                        }
                    }
                ],
                "security": [
                    {
                        "apikey": []
                    }
                ],
                "tags": ["tags"]                      
            },
        },
        "/history/{tag_id}": {
            "get": {
                "responses": {
                    200: {
                        "description": "Success"
                    }
                },
                "parameters": [
                    {
                        "name": "tag_id",
                        "required": True,
                        "in": "path",
                        "type": "string"
                    }
                ],
                "security": [
                    {
                        "apikey": []
                    }
                ],
                "tags": ["history"]
            },
        },
        "/trends": {
            "post": {
                "responses": {
                    200: {
                        "description": "Success"
                    }
                },
                "parameters": [
                    {
                        "name": "payload",
                        "required": True,
                        "in": "body",
                        "schema": {
                            "$ref": "#/definitions/trend_model"
                        }
                    }
                ],
                "security": [
                    {
                        "apikey": []
                    }
                ],
                "tags": ["trends"]
            }
        },
        "/trends/{tag_id}": {
            "parameters": [
                {
                    "name": "tag_id",
                    "required": True,
                    "in": "path",
                    "type": "string"
                }
            ],
            "post": {
                "responses": {
                    200: {
                        "description": "Success"
                    }
                },
                "parameters": [
                    {
                        "name": "payload",
                        "required": True,
                        "in": "body",
                        "schema": {
                            "$ref": "#/definitions/trend_model"
                        }
                    }
                ],
                "security": [
                    {
                        "apikey": []
                    }
                ],
                "tags": ["trends"]
            }
        },
        "/controls": {
            "get": {
                "responses": {
                    200: {
                        "description": "Success"
                    }
                },
                "security": [
                    {
                        "apikey": []
                    }
                ],
                "tags": ["controls"]
            }
        },
        "/controls/{control_name}": {
            "get": {
                "responses": {
                    200: {
                        "description": "Success"
                    }
                },
                "parameters": [
                    {
                        "name": "control_name",
                        "required": True,
                        "in": "path",
                        "type": "string"
                    }
                ],
                "security": [
                    {
                        "apikey": []
                    }
                ],
                "tags": ["controls"] 
            }
        },
        "/rules": {
            "get": {
                "responses": {
                    200: {
                        "description": "Success"
                    }
                },
                "security": [
                    {
                        "apikey": []
                    }
                ],
                "tags": ["controls"]
            }
        },
        "/rules/{rule_name}": {
            "get": {
                "responses": {
                    200: {
                        "description": "Success"
                    }
                },
                "parameters": [
                    {
                        "name": "rule_name",
                        "required": True,
                        "in": "path",
                        "type": "string"
                    }
                ],
                "security": [
                    {
                        "apikey": []
                    }
                ],
                "tags": ["controls"] 
            }
        },
        "/alarms": {
            "get": {
                "responses": {
                    200: {
                        "description": "Success"
                    }
                },
                "security": [
                    {
                        "apikey": []
                    }
                ],
                "tags": ["alarms"]
            }
        },
        "/alarms/{alarm_name}": {
            "get": {
                "responses": {
                    200: {
                        "description": "Success"
                    }
                },
                "parameters": [
                    {
                        "name": "alarm_name",
                        "required": True,
                        "in": "path",
                        "type": "string"
                    }
                ],
                "security": [
                    {
                        "apikey": []
                    }
                ],
                "tags": ["alarms"] 
            },
            "post": {
                "responses": {
                        200: {
                            "description": "Success"
                        }
                    },
                "parameters": [
                    {
                        "name": "alarm_name",
                        "required": True,
                        "in": "path",
                        "type": "string"
                    },
                    {
                        "name": "payload",
                        "required": True,
                        "in": "body",
                        "schema": {
                            "$ref": "#/definitions/alarm_model"
                        }
                    }
                ],
                "security": [
                    {
                        "apikey": []
                    }
                ],
                "tags": ["alarms"]
            }
        },
        "/events": {
            "get": {
                "responses": {
                    200: {
                        "description": "Success"
                    }
                },
                "tags": ["events"]
            },
            "post": {
                "responses": {
                        200: {
                            "description": "Success"
                        }
                    },
                "parameters": [
                    {
                        "name": "payload",
                        "required": True,
                        "in": "body",
                        "schema": {
                            "$ref": "#/definitions/event_model"
                        }
                    }
                ],
                "security": [
                    {
                        "apikey": []
                    }
                ],
                "tags": ["events"]
            }
        },
        "/blobs": {
            "post": {
                "responses": {
                    201: {
                        "description": "Success"
                    }
                },
                "consumes": "multipart/form-data",
                "parameters": [
                    {
                        "in": "formData",
                        "name": "name",
                        "type": "string",
                        "required": True
                    },
                    {
                        "in": "formData",
                        "name": "file",
                        "type": "file",
                        "required": True
                    }
                ],
                "security": [
                    {
                        "apikey": []
                    }
                ],
                "tags": ["blobs"]
            }
        },
        "/blobs/{blob_name}": {
            "get": {
                "responses": {
                    200: {
                        "description": "Success"
                    }
                },
                "parameters": [
                    {
                        "name": "blob_name",
                        "required": True,
                        "in": "path",
                        "type": "string"
                    }
                ],
                "security": [
                    {
                        "apikey": []
                    }
                ],
                "tags": ["blobs"] 
            }
        },
        "/summary": {

        }
    },
    "info": {
        "title": "Rackio Engine API",
        "version": "1.0",
        "description": "Rackio Engine RESTful API for system integration"
    },
    "produces": ["application/json"],
    "consumes": ["application/json", "multipart/form-data"],
    "securityDefinitions": {
        "apikey": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization"
        }
    },
    "tags": [
        {
            "name": "auth",
            "description": "Namespace for authentication"
        },
        {
            "name": "tags",
            "description": "Namespace for tags"
        },
        {
            "name": "history",
            "description": "Namespace for tag history"
        },
        {
            "name": "trends",
            "description": "Namespace for tag trends"
        },
        {
            "name": "controls",
            "description": "Namespace for controls"
        },
        {
            "name": "alarms",
            "description": "Namespace for alarms"
        },
        {
            "name": "events",
            "description": "Namespace for events"
        },
        {
            "name": "blobs",
            "description": "Namespace for blobs"
        },
        {
            "name": "users",
            "description": "Namespace for users"
        }
    ],
    "definitions": {
        "login_model": {
            "required": [
                "password",
                "username"
            ],
            "properties": {
                "username": {
                    "type": "string",
                    "description": "Username"
                },
                "password": {
                    "type": "string",
                    "description": "Password"
                }
            },
            "type": "object"
        },
        "tag_model": {
            "required": ["value"],
            "properties": {
                "value": {
                    "type": "string",
                    "description": "String representation of tag value"
                }
            },
            "type": "object"
        },
        "user_column_model": {
            "required": [
                "field",
                "default"
            ],
            "properties": {
                "field": {
                    "type": "string",
                    "description": "Peewee field type, example ['Char','Integer', 'Text', 'Float', 'Blob', ...]"
                },
                "default": {
                    "type": "string",
                    "description": "Default value"
                },
                "null": {
                    "type": "boolean",
                    "description": "Allow null values"
                }
            },
            "type": "object"
        },
        "user_license_model": {
            "required": [
                "username",
                "license_type"
            ],
            "properties": {
                "username": {
                    "type": "string",
                    "description": "User to whom the license is generated"
                },
                "license_type": {
                    "type": "string",
                    "description": "license type"
                }
            },
            "type": "object"
        },
        "license_model": {
            "required": [
                "license"
            ],
            "properties": {
                "license": {
                    "type": "string",
                    "description": "License type"
                }
            },
            "type": "object"
        },
        "trend_model": {
            "required": ["tags", "tstart", "tstop"],
            "properties": {
                "tags": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "List of Strings representing tag names"
                },
                "tstart": {
                    "type": "string",
                    "description": "Start time for trend (format: %Y-%m-%d %H:%M:%S)"
                },
                "tstop": {
                    "type": "string",
                    "description": "Start time for trend (format: %Y-%m-%d %H:%M:%S)"
                },
            },
            "type": "object"
        },
        "alarm_model": {
            "required": ["action"],
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Action to perform on Alarm 'Acknowledge', 'Disable', 'Enable' or 'Reset'."
                }
            },
            "type": "object"
        },
        "event_model": {
            "required": ["user", "message", "description", "priority"],
            "properties": {
                "user": {
                    "type": "string",
                    "description": "Username logging the event"
                },
                "message": {
                    "type": "string",
                    "description": "Event short message"
                },
                "description": {
                    "type": "string",
                    "description": "Event description"
                },
                "priority": {
                    "type": "integer",
                    "description": "Event priority"
                },
            },
            "type": "object"
        }
    }
}