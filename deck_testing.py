import deck_builder as db
import pytest


## test card class
# construct blank card with no linkages



def test_card():

    card = db.Card()

    # test general attributes
    assert len(card) == 1

    # test attributes of blank card
    assert card.suit == 'None'
    assert card.name == 'None'
    assert card.next == None
    assert card.prev == None
    assert print(card) == None

    # try to define error-producing attributes
    with pytest.raises(TypeError):
        card.set_next("Not a Card")
    with pytest.raises(TypeError):
        card.set_next(0)

    # test proper attribute definitions


