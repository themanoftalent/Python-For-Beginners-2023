from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
        help = "Exports a gettext file to translate the country names (only translation without header)"
        
        def handle_noargs(self, **options):
            from django.utils.encoding import smart_str
            from ...models import Country
            for country in Country.objects.all():
                print '# country', smart_str(country.iso)
                print 'msgid "%s"' % smart_str(country.printable_name.replace('"', '\\"'))
                print 'msgstr ""'
                print ''
