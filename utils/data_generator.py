"""Helpers for generating test data.

Tests should not use hard-coded names/emails. Instead we generate fresh,
realistic data on every run using the ``faker`` library, so re-running a test
never collides with data created by a previous run.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass

from faker import Faker

# One shared Faker instance.
_faker = Faker("en_US")


@dataclass
class Employee:
    """The data needed to add an employee in the PIM module."""

    first_name: str
    middle_name: str
    last_name: str


@dataclass
class Candidate:
    """The data needed to add a recruitment candidate."""

    first_name: str
    last_name: str
    email: str
    phone: str
    vacancy: str


def generate_employee() -> Employee:
    """Create a brand-new random employee.

    OrangeHRM assigns the Employee Id automatically, so the name does not need
    to be unique -- but we still randomise it so each run uses fresh data.
    """
    return Employee(
        first_name=_faker.first_name(),
        middle_name=_faker.first_name(),
        last_name=_faker.last_name(),

    )

VALID_VACANCIES = ["Sales Representative", "qa intern", "Software Engineer", "sr tester", "Senior QA Lead" , "Senior support specialist"]

def generate_candidate() -> Candidate:
    """Create a brand-new random candidate with a guaranteed-unique email."""
    first_name = _faker.first_name()
    last_name = _faker.last_name()
    phone=_faker.phone_number()
    # A UUID fragment keeps the email unique across runs.
    unique = uuid.uuid4().hex[:10]
    email = f"{first_name}.{last_name}.{unique}@example.com".lower()
    vacancy = _faker.random_element(elements=VALID_VACANCIES)
    return Candidate(first_name=first_name, last_name=last_name, email=email, phone=phone, vacancy=vacancy)
