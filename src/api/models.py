from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        nullable=False
    )
    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    role: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    address: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )
    latitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )
    longitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    professional_profile: Mapped["ProfessionalProfile | None"] = relationship(
        back_populates="user",
        uselist=False
    )

    client_requests: Mapped[list["ServiceRequest"]] = relationship(
        back_populates="client",
        foreign_keys="ServiceRequest.client_id"
    )

    professional_requests: Mapped[list["ServiceRequest"]] = relationship(
        back_populates="professional",
        foreign_keys="ServiceRequest.professional_id"
    )

    sent_messages: Mapped[list["Message"]] = relationship(
        back_populates="sender",
        foreign_keys="Message.sender_id"
    )

    received_messages: Mapped[list["Message"]] = relationship(
        back_populates="receiver",
        foreign_keys="Message.receiver_id"
    )

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "address": self.address,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }    


class Category(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    professionals: Mapped[list["ProfessionalProfile"]] = relationship(
        back_populates="category"
    )

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

class ProfessionalProfile(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        unique=True,
        nullable=False
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("category.id"),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    service_area: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    average_rating: Mapped[float] = mapped_column(
        Float,
        default=0.0,
        nullable=False
    )

    user: Mapped["User"] = relationship(
        back_populates="professional_profile"
    )

    category: Mapped["Category"] = relationship(
        back_populates="professionals"
    )

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "category_id": self.category_id,
            "description": self.description,
            "service_area": self.service_area,
            "average_rating": self.average_rating,
            "user": {
                "id": self.user.id,
                "name": self.user.name,
                "address": self.user.address,
                "latitude": self.user.latitude,
                "longitude": self.user.longitude
            } if self.user else None,
            "category": {
                "id": self.category.id,
                "name": self.category.name
            } if self.category else None
        }    

class ServiceRequest(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    client_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        nullable=False
    )

    professional_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="pending",
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    client: Mapped["User"] = relationship(
        back_populates="client_requests",
        foreign_keys=[client_id]
    )

    professional: Mapped["User"] = relationship(
        back_populates="professional_requests",
        foreign_keys=[professional_id]
    )

    messages: Mapped[list["Message"]] = relationship(
        back_populates="service_request"
    )

    review: Mapped["Review | None"] = relationship(
        back_populates="service_request",
        uselist=False
    ) 

    def serialize(self):
        return {
            "id": self.id,
            "client_id": self.client_id,
            "professional_id": self.professional_id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }  

class Message(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    sender_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        nullable=False
    )

    receiver_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        nullable=False
    )

    service_request_id: Mapped[int] = mapped_column(
        ForeignKey("service_request.id"),
        nullable=False
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    sender: Mapped["User"] = relationship(
        back_populates="sent_messages",
        foreign_keys=[sender_id]
    )

    receiver: Mapped["User"] = relationship(
        back_populates="received_messages",
        foreign_keys=[receiver_id]
    )

    service_request: Mapped["ServiceRequest"] = relationship(
        back_populates="messages"
    )

    def serialize(self):
        return {
            "id": self.id,
            "sender_id": self.sender_id,
            "receiver_id": self.receiver_id,
            "service_request_id": self.service_request_id,
            "content": self.content,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }

class Review(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    service_request_id: Mapped[int] = mapped_column(
        ForeignKey("service_request.id"),
        unique=True,
        nullable=False
    )

    rating: Mapped[int] = mapped_column(
        nullable=False
    )

    comment: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    service_request: Mapped["ServiceRequest"] = relationship(
        back_populates="review"
    )

    def serialize(self):
        return {
            "id": self.id,
            "service_request_id": self.service_request_id,
            "rating": self.rating,
            "comment": self.comment,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }