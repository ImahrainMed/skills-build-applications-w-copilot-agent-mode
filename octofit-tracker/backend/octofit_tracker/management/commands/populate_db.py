from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data safely
        for model in [Activity, Leaderboard, Workout, User, Team]:
            qs = model.objects.all()
            if qs.exists():
                qs.delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        captain = User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Create Activities
        Activity.objects.create(user=ironman, type='run', duration=30, distance=5)
        Activity.objects.create(user=batman, type='cycle', duration=60, distance=20)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', suggested_for_team=marvel)
        Workout.objects.create(name='Strength Training', description='Strength for DC heroes', suggested_for_team=dc)

        # Create Leaderboard
        Leaderboard.objects.create(user=ironman, score=100)
        Leaderboard.objects.create(user=batman, score=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
