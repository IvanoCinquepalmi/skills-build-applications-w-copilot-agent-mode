from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Cancella dati esistenti
        get_user_model().objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Crea team
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crea utenti supereroi
        User = get_user_model()
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Crea attività
        Activity.objects.create(user=ironman, type='Running', duration=30, calories=300)
        Activity.objects.create(user=spiderman, type='Cycling', duration=45, calories=400)
        Activity.objects.create(user=batman, type='Swimming', duration=60, calories=500)
        Activity.objects.create(user=superman, type='Yoga', duration=40, calories=200)

        # Crea workout
        Workout.objects.create(name='Full Body', description='Complete workout for all muscles', duration=60)
        Workout.objects.create(name='Cardio Blast', description='High intensity cardio', duration=30)

        # Leaderboard
        Leaderboard.objects.create(user=ironman, points=1000)
        Leaderboard.objects.create(user=spiderman, points=900)
        Leaderboard.objects.create(user=batman, points=950)
        Leaderboard.objects.create(user=superman, points=1100)

        self.stdout.write(self.style.SUCCESS('Database popolato con dati di test!'))
