## Vocera tools
This is a collection of tools written in python to help streamline and/or automate interacting with the Vocera Administrative Console for managing vocera Users, Groups and Devices programmatically. This project relies on python classes to define the attributes and methods associated with the management of each major category (i.e, User, group, device). For convenience, users, groups or devices will henceforth be referred to in this document as Objects of Interest or OIs

### Establishing a Source of Truth
The Vocera Administrative Console lacks a robust API for management functions. As uch, for the sake of convenience, it may be useful to establish an external source of truth outside of the Vocera Administrative Console. This Source of Truth (SoT) may be a csv file, sql database, or some other datastructure which we can interface with 


### Class definitions
Python classes are used in this context for the creation of class instances which represent our OIs. These instances track state information (attribute values; e.g, first name) and our instance methods allow for the modification of attribute information, which will produce changes both within the source of 
