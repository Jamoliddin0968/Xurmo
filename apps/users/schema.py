from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AccessControllerEventModel(BaseModel):
    deviceName: Optional[str] = None
    majorEventType: Optional[int] = None
    subEventType: Optional[int] = None
    cardType: Optional[int] = None
    cardReaderNo: Optional[int] = None
    doorNo: Optional[int] = None
    employeeNo: Optional[int] = None
    employeeNoString: Optional[str] = None
    serialNo: Optional[int] = None
    userType: Optional[str] = None
    attendanceStatus: Optional[str] = None
    statusValue: Optional[int] = None
    picturesNumber: Optional[int] = None

class Event(BaseModel):
    ipAddress: Optional[str] = None
    portNo: Optional[int] = None
    protocol: Optional[str] = None
    dateTime: Optional[datetime] = None
    activePostCount: Optional[int] = None
    eventType: Optional[str] = None
    eventState: Optional[str] = None
    eventDescription: Optional[str] = None
    AccessControllerEvent: Optional[AccessControllerEventModel] = None
