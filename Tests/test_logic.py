import pytest
from appy import Ticket

def test_ticket_has_client_name():
    ticket = Ticket("Cable problem", "Cable is too long", "High")
    assert ticket.client_name == "Cable problem"

def test_complete_ticket_creation():
    ticket = Ticket("Marek", "Computer problem", "High")
    assert ticket.client_name == "Marek"
    assert ticket.problem_description == "Computer problem"
    assert ticket.priority == "High"

def test_ticket_with_empty_description():
    empty_ticket = Ticket("Igor", "", "Low")
    assert empty_ticket.client_name == "Igor"
    assert empty_ticket.problem_description == ""
    assert empty_ticket.priority == "Low"

def test_ticket_with_very_long_client_name():
    long_name = "A" * 500  
    long_ticket = Ticket(long_name, "Problem", "High")
    assert long_ticket.client_name == long_name

def test_status_change_to_resolved():
    ticket_new = Ticket("Margaret", "PLC Failure", "Low")
    assert ticket_new.status == "Open"
    ticket_new.resolve()
    assert ticket_new.status == "Resolved"
def test_new_ticket_is_not_resolved_by_default():
    ticket_new = Ticket("Margaret", "Virus", "High")
    # Test negatywny 
    assert ticket_new.status != "Resolved"