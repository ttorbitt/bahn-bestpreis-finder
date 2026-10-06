"""Pünktlichkeit pro Zug aus piebro/deutsche-bahn-data (CC BY 4.0, Daten: DB Timetables API).
pünktlich = Ankunft weniger als 6 min verspätet (DB-Definition), ausgefallene Halte separat."""
import duckdb, json, sys, gzip
src = sys.argv[1]; out = sys.argv[2]
FV = "('ICE','IC','EC','ECE','RJ','RJX','NJ','EN','FLX','TGV','WB','EST','ES')"
c = duckdb.connect()
q = f"""
with s as (
  select train_type t, ltrim(train_number,'0') nr, line_number ln,
         arrival_planned_time is not null as has_arr,
         coalesce(arrival_is_canceled,false) or coalesce(departure_is_canceled,false) as canc,
         delay_in_min d
  from '{src}' where not coalesce(is_replacement_train,false)
)
select t in {FV} fv, t, nr, any_value(ln) ln,
  count(*) filter (where has_arr and not canc) n,
  round(100.0*avg(case when has_arr and not canc then (d<=5)::int end)) p,
  round(100.0*avg(canc::int)) x
from s group by all having n>=20
"""
rows = c.sql(q).fetchall()
f, r = {}, {}
for fv, t, nr, ln, n, p, x in rows:
    if p is None: continue
    if fv: f[f"{t} {nr}"] = [int(p), int(x)]
    elif ln: r[f"{ln} {nr}"] = [int(p), int(x)]
data = {"m": src.split("data-")[-1][:7], "f": f, "r": r}
s = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
open(out, "w").write(s)
print(len(f), "Fernzüge,", len(r), "Regionalzüge,", len(s)//1024, "KB,", len(gzip.compress(s.encode()))//1024, "KB gzip")
print("ICE 787", f.get("ICE 787"), "RE83 21111", r.get("RE83 21111"), "RE3 82119", r.get("RE3 82119"))
import statistics; print("Median FV", statistics.median(v[0] for v in f.values()), "Median RV", statistics.median(v[0] for v in r.values()))
