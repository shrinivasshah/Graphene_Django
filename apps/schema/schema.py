from graphene_django import DjangoObjectType
import graphene
from apps.users.models import User as UserModel
from apps.decks.models import Deck as DeckModel
from apps.cards.models import Card as CardModel


class UserType(DjangoObjectType):  # TypeDef
    class Meta:
        model = UserModel


class DeckType(DjangoObjectType):  # TypeDef
    class Meta:
        model = DeckModel


class CardType(DjangoObjectType):  # TypeDef
    class Meta:
        model = CardModel


class CreateDeck(graphene.Mutation):
    deck = graphene.Field(DeckType)

    class Arguments:
        title = graphene.String()
        description = graphene.String()

    def mutate(self, info, title, description, deck_id):
        d = DeckModel(title=title, description=description)
        d.save()
        return CreateDeck(deck=d)


class CreateCard(graphene.Mutation):
    card = graphene.Field(CardType)

    class Arguments:
        question = graphene.String()
        answer = graphene.String()
        deck_id = graphene.ID()

    def mutate(self, info, question, answer, deck_id):
        c = CardModel(question=question, answer=answer)
        d = DeckModel.objects.get(id=deck_id)
        c.deck = d
        c.save()
        return CreateCard(card=c)


class Mutation(graphene.ObjectType):
    create_card = CreateCard.Field()
    create_deck = CreateDeck.Field()


class Query(graphene.ObjectType):
    users = graphene.List(UserType)  # resolver attributes
    decks = graphene.List(DeckType)
    cards = graphene.List(CardType)
    deck_by_id = graphene.Field(DeckType, id=graphene.ID())

    def resolve_users(self, info):
        return UserModel.objects.all()

    def resolve_decks(self, info):
        return DeckModel.objects.all()

    def resolve_deck_by_id(self, info, id):
        return DeckModel.objects.get(pk=id)

    def resolve_cards(self, info):
        return CardModel.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutation)
