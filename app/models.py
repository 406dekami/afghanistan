from django.db import models


class AfghanistanPopulation(models.Model):
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population', blank=True, null=True)  # Field name made lowercase.
    yearly_change = models.FloatField(db_column='Yearly %  Change', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    yearly_change_0 = models.IntegerField(db_column='Yearly Change', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because of name conflict.
    migrants_net_field = models.IntegerField(db_column='Migrants (net)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    median_age = models.FloatField(db_column='Median Age', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fertility_rate = models.FloatField(db_column='Fertility Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    density_p_km2_field = models.IntegerField(db_column='Density (P/Km²)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    urban_pop_field = models.FloatField(db_column='Urban Pop %', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    urban_population = models.IntegerField(db_column='Urban Population', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country_s_share_of_world_pop = models.FloatField(db_column="Country's Share of World Pop", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    world_population = models.FloatField(db_column='World Population', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    afghanistanglobal_rank = models.IntegerField(db_column='AfghanistanGlobal Rank', blank=True, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'afghanistan_population'
        verbose_name = '浏览阿富汗人口信息 '
        verbose_name_plural = '阿富汗人口信息管理(不可修改)'
