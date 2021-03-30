# Flask API for Event management

Version: 1.0.0

Run the flask server: Go to Flask API directory and run the following command: python manage.py run

## List of endpoints:

### '/add_event' [POST]

Creates a new event

Body structure example:

```
{

  "name": "string", # required
  
  "start": "string with format %Y-%m-%d %H:%M", # defaults to current date
  
  "stop": "string with format %Y-%m-%d %H:%M", # optional
  
  "tags": ["string", "string", ...] # optional
  
  "any_other_field": Any # optional
  
}
```

start (or stop) example: 2010-01-20 5:20

Only name is required, start defaults to current date.

Any other document field can be added and stored in the mongo database.

### '/list_events' [GET]

Get a list of events with optional filters

Parameters to pass in url:

```
name: string contained in the name, or full name depending on name_exact (default is full)


name_exact: name is exact (True) or partial (False) (default is True)


start_min: filters start date before start_min

format %Y-%m-%d %H:%M, ex: 2010-01-20 5:20



start_max: filters start date after start_max

format %Y-%m-%d %H:%M, ex: 2010-01-20 5:20


stop_min: filters stop date before stop_min

format %Y-%m-%d %H:%M, ex: 2010-01-20 5:20


stop_max: filters stop date after stop_max

format %Y-%m-%d %H:%M, ex: 2010-01-20 5:20


tags: event must have all the mentioned tags

strings separated with commas, ex: red,blue
```


Use '?' to start adding parameters and '&' to separate each of them

**example of url:** api.com/event/list_events?name=new%20event&name_exact=False&start_min=2010-01-20%205:20&tags=blue,red


### '/remove_events' [DELETE]

Delete events with corresponding names

Body structure example:

```
{
  "name_list": ["string", "string", ...]
}
```

Corresponding names (full name) will be deleted from the database.
