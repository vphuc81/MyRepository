.class public Lcom/aces/tv/Splash;
.super Landroid/app/Activity;
.source "Splash.java"


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/aces/tv/Splash$FillCache;,
        Lcom/aces/tv/Splash$DownloadObb;,
        Lcom/aces/tv/Splash$StateMachine;
    }
.end annotation


# static fields
.field private static final Caching:I = 0x5

.field private static final CachingDone:I = 0x6

.field private static final Checking:I = 0x2

.field private static final ChecksDone:I = 0x3

.field private static final Clearing:I = 0x4

.field private static final DownloadObbDone:I = 0x5b

.field private static final DownloadingObb:I = 0x5a

.field private static final InError:I = 0x1

.field private static final StartingXBMC:I = 0x63

.field private static final StorageChecked:I = 0x8

.field private static final TAG:Ljava/lang/String; = "Kodi"

.field private static final Uninitialized:I = 0x0

.field private static final WaitingStorageChecked:I = 0x7


# instance fields
.field private fPackagePath:Ljava/io/File;

.field private fXbmcHome:Ljava/io/File;

.field private mCachingDone:Z

.field private mCpuinfo:Ljava/lang/String;

.field private mErrorMsg:Ljava/lang/String;

.field private mExternalStorageChecked:Z

.field private mExternalStorageReceiver:Landroid/content/BroadcastReceiver;

.field private mInstallLibs:Z

.field private mMounts:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList",
            "<",
            "Ljava/lang/String;",
            ">;"
        }
    .end annotation
.end field

.field private mProgress:Landroid/widget/ProgressBar;

.field private mState:I

.field private mStateMachine:Lcom/aces/tv/Splash$StateMachine;

.field private mTextView:Landroid/widget/TextView;

.field public myAlertDialog:Landroid/app/AlertDialog;

.field private sPackagePath:Ljava/lang/String;

.field private sXbmcHome:Ljava/lang/String;

.field private sXbmcdata:Ljava/lang/String;


# direct methods
.method public constructor <init>()V
    .locals 3

    .prologue
    const/4 v2, 0x0

    const/4 v1, 0x0

    .line 52
    invoke-direct {p0}, Landroid/app/Activity;-><init>()V

    .line 69
    const-string v0, ""

    iput-object v0, p0, Lcom/aces/tv/Splash;->mCpuinfo:Ljava/lang/String;

    .line 70
    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/aces/tv/Splash;->mMounts:Ljava/util/ArrayList;

    .line 71
    const-string v0, ""

    iput-object v0, p0, Lcom/boom/mediai/Splash;->mErrorMsg:Ljava/lang/String;

    .line 73
    iput-object v1, p0, Lcom/aces/tv/Splash;->mProgress:Landroid/widget/ProgressBar;

    .line 74
    iput-object v1, p0, Lcom/aces/tv/Splash;->mTextView:Landroid/widget/TextView;

    .line 76
    iput v2, p0, Lcom/aces/tv/Splash;->mState:I

    .line 79
    const-string v0, ""

    iput-object v0, p0, Lcom/aces/tv/Splash;->sPackagePath:Ljava/lang/String;

    .line 80
    const-string v0, ""

    iput-object v0, p0, Lcom/aces/tv/Splash;->sXbmcHome:Ljava/lang/String;

    .line 81
    const-string v0, ""

    iput-object v0, p0, Lcom/aces/tv/Splash;->sXbmcdata:Ljava/lang/String;

    .line 82
    iput-object v1, p0, Lcom/aces/tv/Splash;->fPackagePath:Ljava/io/File;

    .line 83
    iput-object v1, p0, Lcom/aces/tv/Splash;->fXbmcHome:Ljava/io/File;

    .line 85
    iput-object v1, p0, Lcom/aces/tv/Splash;->mExternalStorageReceiver:Landroid/content/BroadcastReceiver;

    .line 86
    iput-boolean v2, p0, Lcom/aces/tv/Splash;->mExternalStorageChecked:Z

    .line 87
    iput-boolean v2, p0, Lcom/aces/tv/Splash;->mCachingDone:Z

    .line 88
    iput-boolean v2, p0, Lcom/aces/tv/Splash;->mInstallLibs:Z

    .line 159
    new-instance v0, Lcom/aces/tv/Splash$StateMachine;

    invoke-direct {v0, p0, p0}, Lcom/aces/tv/Splash$StateMachine;-><init>(Lcom/aces/tv/Splash;Lcom/aces/tv/Splash;)V

    iput-object v0, p0, Lcom/aces/tv/Splash;->mStateMachine:Lcom/aces/tv/Splash$StateMachine;

    .line 273
    return-void
.end method

.method private CheckCpuFeature(Ljava/lang/String;)Z
    .locals 2

    .prologue
    .line 619
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "(?i):.*?\\s"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, "(?:\\s|$)"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Ljava/util/regex/Pattern;->compile(Ljava/lang/String;)Ljava/util/regex/Pattern;

    move-result-object v0

    .line 620
    iget-object v1, p0, Lcom/aces/tv/Splash;->mCpuinfo:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/util/regex/Pattern;->matcher(Ljava/lang/CharSequence;)Ljava/util/regex/Matcher;

    move-result-object v0

    .line 621
    invoke-virtual {v0}, Ljava/util/regex/Matcher;->find()Z

    move-result v0

    return v0
.end method

.method private MigrateUserData()V
    .locals 6

    .prologue
    const/4 v2, 0x0

    .line 522
    :try_start_0
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const/4 v1, 0x0

    invoke-virtual {p0, v1}, Lcom/aces/tv/Splash;->getExternalFilesDir(Ljava/lang/String;)Ljava/io/File;

    move-result-object v1

    invoke-virtual {v1}, Ljava/io/File;->getParentFile()Ljava/io/File;

    move-result-object v1

    invoke-virtual {v1}, Ljava/io/File;->getParentFile()Ljava/io/File;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, "/org.xbmc.xbmc/files/.xbmc"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    .line 523
    new-instance v1, Ljava/io/File;

    invoke-direct {v1, v0}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    .line 524
    invoke-virtual {v1}, Ljava/io/File;->exists()Z
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_1

    move-result v0

    if-nez v0, :cond_1

    .line 552
    :cond_0
    :goto_0
    return-void

    .line 530
    :cond_1
    new-instance v0, Ljava/io/File;

    invoke-virtual {p0, v2}, Lcom/aces/tv/Splash;->getExternalFilesDir(Ljava/lang/String;)Ljava/io/File;

    move-result-object v2

    const-string v3, ".kodi"

    invoke-direct {v0, v2, v3}, Ljava/io/File;-><init>(Ljava/io/File;Ljava/lang/String;)V

    .line 531
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0}, Ljava/io/File;->getAbsolutePath()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, "/.kodi_data_was_migrated"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    .line 532
    new-instance v3, Ljava/io/File;

    invoke-direct {v3, v2}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    .line 534
    const-string v2, "Kodi"

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, "External_dir = "

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-static {v2, v4}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 535
    invoke-virtual {v1}, Ljava/io/File;->exists()Z

    move-result v2

    if-eqz v2, :cond_0

    invoke-virtual {v0}, Ljava/io/File;->exists()Z

    move-result v2

    if-nez v2, :cond_0

    .line 536
    const-string v2, "Kodi"

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, "XBMC user data detected at "

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v1}, Ljava/io/File;->getAbsolutePath()Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    const-string v5, ", migrating to "

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v0}, Ljava/io/File;->getAbsolutePath()Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-static {v2, v4}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 537
    invoke-virtual {v0}, Ljava/io/File;->getParentFile()Ljava/io/File;

    move-result-object v2

    invoke-virtual {v2}, Ljava/io/File;->exists()Z

    move-result v2

    if-nez v2, :cond_2

    invoke-virtual {v0}, Ljava/io/File;->getParentFile()Ljava/io/File;

    move-result-object v2

    invoke-virtual {v2}, Ljava/io/File;->mkdirs()Z

    move-result v2

    if-nez v2, :cond_2

    .line 538
    const-string v1, "Kodi"

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "Error creating "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v0}, Ljava/io/File;->getParentFile()Ljava/io/File;

    move-result-object v0

    invoke-virtual {v0}, Ljava/io/File;->getAbsolutePath()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto/16 :goto_0

    .line 541
    :cond_2
    invoke-virtual {v1, v0}, Ljava/io/File;->renameTo(Ljava/io/File;)Z

    move-result v0

    if-eqz v0, :cond_3

    .line 543
    :try_start_1
    new-instance v0, Ljava/io/FileOutputStream;

    invoke-direct {v0, v3}, Ljava/io/FileOutputStream;-><init>(Ljava/io/File;)V

    invoke-virtual {v0}, Ljava/io/FileOutputStream;->close()V
    :try_end_1
    .catch Ljava/io/IOException; {:try_start_1 .. :try_end_1} :catch_0

    .line 547
    :goto_1
    const-string v0, "Kodi"

    const-string v1, "XBMC user data migrated to Kodi successfully"

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto/16 :goto_0

    .line 544
    :catch_0
    move-exception v0

    .line 545
    invoke-virtual {v0}, Ljava/io/IOException;->printStackTrace()V

    goto :goto_1

    .line 549
    :cond_3
    const-string v0, "Kodi"

    const-string v1, "Error migrating XBMC user data"

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto/16 :goto_0

    .line 526
    :catch_1
    move-exception v0

    goto/16 :goto_0
.end method

.method private ParseCpuFeature()Z
    .locals 6

    .prologue
    const/4 v0, 0x1

    const/4 v1, 0x0

    .line 559
    const/4 v2, 0x2

    :try_start_0
    new-array v2, v2, [Ljava/lang/String;

    const/4 v3, 0x0

    const-string v4, "/system/bin/cat"

    aput-object v4, v2, v3

    const/4 v3, 0x1

    const-string v4, "/proc/cpuinfo"

    aput-object v4, v2, v3

    .line 560
    new-instance v3, Ljava/lang/ProcessBuilder;

    invoke-direct {v3, v2}, Ljava/lang/ProcessBuilder;-><init>([Ljava/lang/String;)V

    .line 562
    invoke-virtual {v3}, Ljava/lang/ProcessBuilder;->start()Ljava/lang/Process;

    move-result-object v2

    .line 563
    invoke-virtual {v2}, Ljava/lang/Process;->getInputStream()Ljava/io/InputStream;

    move-result-object v2

    .line 564
    const/16 v3, 0x400

    new-array v3, v3, [B

    .line 565
    :goto_0
    invoke-virtual {v2, v3}, Ljava/io/InputStream;->read([B)I

    move-result v4

    const/4 v5, -0x1

    if-eq v4, v5, :cond_0

    .line 566
    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v5, p0, Lcom/aces/tv/Splash;->mCpuinfo:Ljava/lang/String;

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    new-instance v5, Ljava/lang/String;

    invoke-direct {v5, v3}, Ljava/lang/String;-><init>([B)V

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    iput-object v4, p0, Lcom/aces/tv/Splash;->mCpuinfo:Ljava/lang/String;
    :try_end_0
    .catch Ljava/io/IOException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    .line 569
    :catch_0
    move-exception v0

    .line 570
    invoke-virtual {v0}, Ljava/io/IOException;->printStackTrace()V

    move v0, v1

    .line 573
    :goto_1
    return v0

    .line 568
    :cond_0
    :try_start_1
    invoke-virtual {v2}, Ljava/io/InputStream;->close()V
    :try_end_1
    .catch Ljava/io/IOException; {:try_start_1 .. :try_end_1} :catch_0

    goto :goto_1
.end method

.method private ParseMounts()Z
    .locals 9

    .prologue
    const/4 v1, 0x1

    const/4 v0, 0x0

    const/4 v8, 0x2

    .line 585
    const-string v2, "^(.+?)\\s+(.+?)\\s+(.+?)\\s"

    invoke-static {v2}, Ljava/util/regex/Pattern;->compile(Ljava/lang/String;)Ljava/util/regex/Pattern;

    move-result-object v3

    .line 586
    const-string v2, ""

    .line 589
    const/4 v4, 0x2

    :try_start_0
    new-array v4, v4, [Ljava/lang/String;

    const/4 v5, 0x0

    const-string v6, "/system/bin/cat"

    aput-object v6, v4, v5

    const/4 v5, 0x1

    const-string v6, "/proc/mounts"

    aput-object v6, v4, v5

    .line 590
    new-instance v5, Ljava/lang/ProcessBuilder;

    invoke-direct {v5, v4}, Ljava/lang/ProcessBuilder;-><init>([Ljava/lang/String;)V

    .line 592
    invoke-virtual {v5}, Ljava/lang/ProcessBuilder;->start()Ljava/lang/Process;

    move-result-object v4

    .line 593
    invoke-virtual {v4}, Ljava/lang/Process;->getInputStream()Ljava/io/InputStream;

    move-result-object v4

    .line 594
    const/16 v5, 0x400

    new-array v5, v5, [B

    .line 595
    :goto_0
    invoke-virtual {v4, v5}, Ljava/io/InputStream;->read([B)I

    move-result v6

    const/4 v7, -0x1

    if-eq v6, v7, :cond_0

    .line 596
    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v6, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    new-instance v6, Ljava/lang/String;

    invoke-direct {v6, v5}, Ljava/lang/String;-><init>([B)V

    invoke-virtual {v2, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    goto :goto_0

    .line 598
    :cond_0
    invoke-virtual {v4}, Ljava/io/InputStream;->close()V
    :try_end_0
    .catch Ljava/io/IOException; {:try_start_0 .. :try_end_0} :catch_0

    .line 604
    const-string v4, "\n"

    invoke-virtual {v2, v4}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v2

    .line 605
    :goto_1
    array-length v4, v2

    if-ge v0, v4, :cond_2

    .line 606
    const-string v4, "Kodi"

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "mount: "

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    aget-object v6, v2, v0

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-static {v4, v5}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 607
    aget-object v4, v2, v0

    invoke-virtual {v3, v4}, Ljava/util/regex/Pattern;->matcher(Ljava/lang/CharSequence;)Ljava/util/regex/Matcher;

    move-result-object v4

    .line 608
    invoke-virtual {v4}, Ljava/util/regex/Matcher;->find()Z

    move-result v5

    if-eqz v5, :cond_1

    .line 609
    invoke-virtual {v4, v1}, Ljava/util/regex/Matcher;->group(I)Ljava/lang/String;

    move-result-object v5

    const-string v6, "/dev/block/vold"

    invoke-virtual {v5, v6}, Ljava/lang/String;->startsWith(Ljava/lang/String;)Z

    move-result v5

    if-eqz v5, :cond_1

    invoke-virtual {v4, v8}, Ljava/util/regex/Matcher;->group(I)Ljava/lang/String;

    move-result-object v5

    const-string v6, "/mnt/secure/asec"

    invoke-virtual {v5, v6}, Ljava/lang/String;->startsWith(Ljava/lang/String;)Z

    move-result v5

    if-nez v5, :cond_1

    .line 610
    const-string v5, "Kodi"

    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    const-string v7, "addind mount: "

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v4, v8}, Ljava/util/regex/Matcher;->group(I)Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    invoke-static {v5, v6}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 611
    iget-object v5, p0, Lcom/aces/tv/Splash;->mMounts:Ljava/util/ArrayList;

    invoke-virtual {v4, v8}, Ljava/util/regex/Matcher;->group(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    .line 605
    :cond_1
    add-int/lit8 v0, v0, 0x1

    goto :goto_1

    .line 599
    :catch_0
    move-exception v1

    .line 600
    invoke-virtual {v1}, Ljava/io/IOException;->printStackTrace()V

    .line 615
    :goto_2
    return v0

    :cond_2
    move v0, v1

    goto :goto_2
.end method

.method private SetupEnvironment()V
    .locals 7

    .prologue
    const/16 v0, 0x14

    const/4 v6, 0x0

    .line 430
    new-instance v1, Ljava/io/File;

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-static {}, Landroid/os/Environment;->getExternalStorageDirectory()Ljava/io/File;

    move-result-object v3

    invoke-virtual {v3}, Ljava/io/File;->getAbsolutePath()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, "/xbmc_env.properties"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-direct {v1, v2}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    .line 431
    invoke-virtual {v1}, Ljava/io/File;->exists()Z

    move-result v2

    if-eqz v2, :cond_3

    .line 432
    const-string v2, "Kodi"

    const-string v3, "Loading xbmc_env.properties"

    invoke-static {v2, v3}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    .line 434
    :try_start_0
    new-instance v2, Ljava/util/Properties;

    invoke-static {}, Ljava/lang/System;->getProperties()Ljava/util/Properties;

    move-result-object v3

    invoke-direct {v2, v3}, Ljava/util/Properties;-><init>(Ljava/util/Properties;)V

    .line 435
    new-instance v3, Ljava/io/FileInputStream;

    invoke-direct {v3, v1}, Ljava/io/FileInputStream;-><init>(Ljava/io/File;)V

    .line 436
    invoke-virtual {v2, v3}, Ljava/util/Properties;->load(Ljava/io/InputStream;)V

    .line 437
    invoke-static {v2}, Ljava/lang/System;->setProperties(Ljava/util/Properties;)V

    .line 439
    const-string v1, "xbmc.home"

    const-string v2, ""

    invoke-static {v1, v2}, Ljava/lang/System;->getProperty(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    iput-object v1, p0, Lcom/aces/tv/Splash;->sXbmcHome:Ljava/lang/String;

    .line 440
    iget-object v1, p0, Lcom/aces/tv/Splash;->sXbmcHome:Ljava/lang/String;

    invoke-virtual {v1}, Ljava/lang/String;->isEmpty()Z

    move-result v1

    if-nez v1, :cond_1

    .line 441
    new-instance v2, Ljava/io/File;

    iget-object v1, p0, Lcom/aces/tv/Splash;->sXbmcHome:Ljava/lang/String;

    invoke-direct {v2, v1}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    move v1, v0

    .line 443
    :goto_0
    invoke-virtual {v2}, Ljava/io/File;->exists()Z
    :try_end_0
    .catch Landroid/content/res/Resources$NotFoundException; {:try_start_0 .. :try_end_0} :catch_0
    .catch Ljava/io/IOException; {:try_start_0 .. :try_end_0} :catch_1

    move-result v3

    if-nez v3, :cond_0

    if-lez v1, :cond_0

    .line 446
    const-wide/16 v4, 0x3e8

    :try_start_1
    invoke-static {v4, v5}, Ljava/lang/Thread;->sleep(J)V
    :try_end_1
    .catch Ljava/lang/InterruptedException; {:try_start_1 .. :try_end_1} :catch_2
    .catch Landroid/content/res/Resources$NotFoundException; {:try_start_1 .. :try_end_1} :catch_0
    .catch Ljava/io/IOException; {:try_start_1 .. :try_end_1} :catch_1

    .line 450
    add-int/lit8 v1, v1, -0x1

    goto :goto_0

    .line 452
    :cond_0
    :try_start_2
    invoke-virtual {v2}, Ljava/io/File;->exists()Z

    move-result v1

    if-nez v1, :cond_1

    .line 453
    const-string v1, "xbmc.home"

    const-string v2, ""

    invoke-static {v1, v2}, Ljava/lang/System;->setProperty(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    .line 454
    const-string v1, ""

    iput-object v1, p0, Lcom/aces/tv/Splash;->sXbmcHome:Ljava/lang/String;

    .line 458
    :cond_1
    const-string v1, "xbmc.data"

    const-string v2, ""

    invoke-static {v1, v2}, Ljava/lang/System;->getProperty(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    iput-object v1, p0, Lcom/aces/tv/Splash;->sXbmcdata:Ljava/lang/String;

    .line 459
    iget-object v1, p0, Lcom/aces/tv/Splash;->sXbmcdata:Ljava/lang/String;

    invoke-virtual {v1}, Ljava/lang/String;->isEmpty()Z

    move-result v1

    if-nez v1, :cond_3

    .line 460
    new-instance v1, Ljava/io/File;

    iget-object v2, p0, Lcom/aces/tv/Splash;->sXbmcdata:Ljava/lang/String;

    invoke-direct {v1, v2}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    .line 462
    :goto_1
    invoke-virtual {v1}, Ljava/io/File;->exists()Z
    :try_end_2
    .catch Landroid/content/res/Resources$NotFoundException; {:try_start_2 .. :try_end_2} :catch_0
    .catch Ljava/io/IOException; {:try_start_2 .. :try_end_2} :catch_1

    move-result v2

    if-nez v2, :cond_2

    if-lez v0, :cond_2

    .line 465
    const-wide/16 v2, 0x3e8

    :try_start_3
    invoke-static {v2, v3}, Ljava/lang/Thread;->sleep(J)V
    :try_end_3
    .catch Ljava/lang/InterruptedException; {:try_start_3 .. :try_end_3} :catch_3
    .catch Landroid/content/res/Resources$NotFoundException; {:try_start_3 .. :try_end_3} :catch_0
    .catch Ljava/io/IOException; {:try_start_3 .. :try_end_3} :catch_1

    .line 469
    add-int/lit8 v0, v0, -0x1

    goto :goto_1

    .line 472
    :cond_2
    :try_start_4
    invoke-virtual {v1}, Ljava/io/File;->exists()Z

    move-result v0

    if-nez v0, :cond_3

    .line 473
    const-string v0, ""

    iput-object v0, p0, Lcom/aces/tv/Splash;->sXbmcdata:Ljava/lang/String;

    .line 474
    const-string v0, "xbmc.data"

    const-string v1, ""

    invoke-static {v0, v1}, Ljava/lang/System;->setProperty(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    :try_end_4
    .catch Landroid/content/res/Resources$NotFoundException; {:try_start_4 .. :try_end_4} :catch_0
    .catch Ljava/io/IOException; {:try_start_4 .. :try_end_4} :catch_1

    .line 484
    :cond_3
    :goto_2
    iget-object v0, p0, Lcom/aces/tv/Splash;->sXbmcHome:Ljava/lang/String;

    invoke-virtual {v0}, Ljava/lang/String;->isEmpty()Z

    move-result v0

    if-eqz v0, :cond_4

    .line 485
    invoke-virtual {p0}, Lcom/aces/tv/Splash;->getCacheDir()Ljava/io/File;

    move-result-object v0

    .line 486
    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0}, Ljava/io/File;->getAbsolutePath()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, "/apk"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/aces/tv/Splash;->sXbmcHome:Ljava/lang/String;

    .line 489
    :cond_4
    new-instance v0, Ljava/io/File;

    iget-object v1, p0, Lcom/aces/tv/Splash;->sXbmcHome:Ljava/lang/String;

    invoke-direct {v0, v1}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    iput-object v0, p0, Lcom/aces/tv/Splash;->fXbmcHome:Ljava/io/File;

    .line 491
    invoke-virtual {p0}, Lcom/aces/tv/Splash;->getPackageResourcePath()Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/aces/tv/Splash;->sPackagePath:Ljava/lang/String;

    .line 492
    new-instance v0, Ljava/io/File;

    iget-object v1, p0, Lcom/aces/tv/Splash;->sPackagePath:Ljava/lang/String;

    invoke-direct {v0, v1}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    iput-object v0, p0, Lcom/aces/tv/Splash;->fPackagePath:Ljava/io/File;

    .line 493
    const-string v0, ""

    .line 494
    iget-object v1, p0, Lcom/aces/tv/Splash;->fPackagePath:Ljava/io/File;

    invoke-virtual {v1}, Ljava/io/File;->length()J

    move-result-wide v2

    const-wide/32 v4, 0x3200000

    cmp-long v1, v2, v4

    if-gez v1, :cond_7

    .line 496
    const-string v1, "Kodi.obb"

    const-string v2, ""

    invoke-static {v1, v2}, Ljava/lang/System;->getProperty(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    iput-object v1, p0, Lcom/aces/tv/Splash;->sPackagePath:Ljava/lang/String;

    .line 497
    iget-object v1, p0, Lcom/aces/tv/Splash;->sPackagePath:Ljava/lang/String;

    const-string v2, ""

    invoke-virtual {v1, v2}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_5

    .line 501
    :try_start_5
    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "main."

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {p0}, Lcom/aces/tv/Splash;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v2

    invoke-virtual {p0}, Lcom/aces/tv/Splash;->getPackageName()Ljava/lang/String;

    move-result-object v3

    const/4 v4, 0x0

    invoke-virtual {v2, v3, v4}, Landroid/content/pm/PackageManager;->getPackageInfo(Ljava/lang/String;I)Landroid/content/pm/PackageInfo;

    move-result-object v2

    iget v2, v2, Landroid/content/pm/PackageInfo;->versionCode:I

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v1

    const-string v2, "."

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {p0}, Lcom/aces/tv/Splash;->getPackageName()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    const-string v2, ".obb"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    .line 502
    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    invoke-static {}, Landroid/os/Environment;->getExternalStorageDirectory()Ljava/io/File;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v1

    const-string v2, "/Android/obb/"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {p0}, Lcom/aces/tv/Splash;->getPackageName()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    const-string v2, "/"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    iput-object v1, p0, Lcom/aces/tv/Splash;->sPackagePath:Ljava/lang/String;
    :try_end_5
    .catch Ljava/lang/Exception; {:try_start_5 .. :try_end_5} :catch_4

    .line 507
    :cond_5
    :goto_3
    new-instance v1, Ljava/io/File;

    iget-object v2, p0, Lcom/aces/tv/Splash;->sPackagePath:Ljava/lang/String;

    invoke-direct {v1, v2}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    iput-object v1, p0, Lcom/aces/tv/Splash;->fPackagePath:Ljava/io/File;

    .line 508
    iget-object v1, p0, Lcom/aces/tv/Splash;->fPackagePath:Ljava/io/File;

    invoke-virtual {v1}, Ljava/io/File;->length()J

    move-result-wide v2

    const-wide/32 v4, 0xa00000

    cmp-long v1, v2, v4

    if-gez v1, :cond_6

    .line 509
    iget-object v1, p0, Lcom/aces/tv/Splash;->fPackagePath:Ljava/io/File;

    invoke-virtual {v1}, Ljava/io/File;->delete()Z

    .line 510
    :cond_6
    iget-object v1, p0, Lcom/aces/tv/Splash;->fPackagePath:Ljava/io/File;

    invoke-virtual {v1}, Ljava/io/File;->exists()Z

    move-result v1

    if-nez v1, :cond_7

    .line 512
    const/16 v1, 0x5a

    iput v1, p0, Lcom/aces/tv/Splash;->mState:I

    .line 513
    new-instance v1, Lcom/aces/tv/Splash$DownloadObb;

    invoke-direct {v1, p0, p0}, Lcom/aces/tv/Splash$DownloadObb;-><init>(Lcom/aces/tv/Splash;Lcom/aces/tv/Splash;)V

    const/4 v2, 0x2

    new-array v2, v2, [Ljava/lang/String;

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "http://mirrors.kodi.tv/releases/android/obb/"

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    aput-object v0, v2, v6

    const/4 v0, 0x1

    iget-object v3, p0, Lcom/aces/tv/Splash;->sPackagePath:Ljava/lang/String;

    aput-object v3, v2, v0

    invoke-virtual {v1, v2}, Lcom/aces/tv/Splash$DownloadObb;->execute([Ljava/lang/Object;)Landroid/os/AsyncTask;

    .line 516
    :cond_7
    return-void

    .line 478
    :catch_0
    move-exception v0

    .line 479
    const-string v0, "Kodi"

    const-string v1, "Cannot find xbmc_env properties file"

    invoke-static {v0, v1}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    goto/16 :goto_2

    .line 480
    :catch_1
    move-exception v0

    .line 481
    const-string v0, "Kodi"

    const-string v1, "Failed to open xbmc_env properties file"

    invoke-static {v0, v1}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    goto/16 :goto_2

    .line 447
    :catch_2
    move-exception v3

    goto/16 :goto_0

    .line 466
    :catch_3
    move-exception v2

    goto/16 :goto_1

    .line 504
    :catch_4
    move-exception v1

    goto :goto_3
.end method

.method static synthetic access$000(Lcom/aces/tv/Splash;)I
    .locals 1

    .prologue
    .line 52
    iget v0, p0, Lcom/aces/tv/Splash;->mState:I

    return v0
.end method

.method static synthetic access$002(Lcom/aces/tv/Splash;I)I
    .locals 0

    .prologue
    .line 52
    iput p1, p0, Lcom/aces/tv/Splash;->mState:I

    return p1
.end method

.method static synthetic access$100(Lcom/aces/tv/Splash;)Ljava/lang/String;
    .locals 1

    .prologue
    .line 52
    iget-object v0, p0, Lcom/aces/tv/Splash;->mErrorMsg:Ljava/lang/String;

    return-object v0
.end method

.method static synthetic access$1000(Lcom/aces/tv/Splash;)Lcom/aces/tv/Splash$StateMachine;
    .locals 1

    .prologue
    .line 52
    iget-object v0, p0, Lcom/aces/tv/Splash;->mStateMachine:Lcom/aces/tv/Splash$StateMachine;

    return-object v0
.end method

.method static synthetic access$102(Lcom/aces/tv/Splash;Ljava/lang/String;)Ljava/lang/String;
    .locals 0

    .prologue
    .line 52
    iput-object p1, p0, Lcom/aces/tv/Splash;->mErrorMsg:Ljava/lang/String;

    return-object p1
.end method

.method static synthetic access$1100(Lcom/aces/tv/Splash;)Ljava/lang/String;
    .locals 1

    .prologue
    .line 52
    iget-object v0, p0, Lcom/aces/tv/Splash;->sPackagePath:Ljava/lang/String;

    return-object v0
.end method

.method static synthetic access$1200(Lcom/aces/tv/Splash;)Ljava/lang/String;
    .locals 1

    .prologue
    .line 52
    iget-object v0, p0, Lcom/aces/tv/Splash;->sXbmcHome:Ljava/lang/String;

    return-object v0
.end method

.method static synthetic access$200(Lcom/aces/tv/Splash;)Landroid/widget/TextView;
    .locals 1

    .prologue
    .line 52
    iget-object v0, p0, Lcom/aces/tv/Splash;->mTextView:Landroid/widget/TextView;

    return-object v0
.end method

.method static synthetic access$300(Lcom/aces/tv/Splash;)Landroid/widget/ProgressBar;
    .locals 1

    .prologue
    .line 52
    iget-object v0, p0, Lcom/aces/tv/Splash;->mProgress:Landroid/widget/ProgressBar;

    return-object v0
.end method

.method static synthetic access$400(Lcom/aces/tv/Splash;)Z
    .locals 1

    .prologue
    .line 52
    iget-boolean v0, p0, Lcom/aces/tv/Splash;->mCachingDone:Z

    return v0
.end method

.method static synthetic access$402(Lcom/aces/tv/Splash;Z)Z
    .locals 0

    .prologue
    .line 52
    iput-boolean p1, p0, Lcom/aces/tv/Splash;->mCachingDone:Z

    return p1
.end method

.method static synthetic access$502(Lcom/aces/tv/Splash;Z)Z
    .locals 0

    .prologue
    .line 52
    iput-boolean p1, p0, Lcom/aces/tv/Splash;->mExternalStorageChecked:Z

    return p1
.end method

.method static synthetic access$600(Lcom/aces/tv/Splash;)V
    .locals 0

    .prologue
    .line 52
    invoke-direct {p0}, Lcom/aces/tv/Splash;->SetupEnvironment()V

    return-void
.end method

.method static synthetic access$700(Lcom/aces/tv/Splash;)Ljava/io/File;
    .locals 1

    .prologue
    .line 52
    iget-object v0, p0, Lcom/aces/tv/Splash;->fXbmcHome:Ljava/io/File;

    return-object v0
.end method

.method static synthetic access$800(Lcom/aces/tv/Splash;)Ljava/io/File;
    .locals 1

    .prologue
    .line 52
    iget-object v0, p0, Lcom/aces/tv/Splash;->fPackagePath:Ljava/io/File;

    return-object v0
.end method

.method static synthetic access$900(Lcom/aces/tv/Splash;)Z
    .locals 1

    .prologue
    .line 52
    iget-boolean v0, p0, Lcom/aces/tv/Splash;->mInstallLibs:Z

    return v0
.end method


# virtual methods
.method public onCreate(Landroid/os/Bundle;)V
    .locals 11

    .prologue
    const/4 v10, 0x6

    const/16 v9, 0x5a

    const/4 v2, 0x0

    const/4 v4, 0x1

    .line 668
    invoke-super {p0, p1}, Landroid/app/Activity;->onCreate(Landroid/os/Bundle;)V

    .line 671
    invoke-virtual {p0}, Lcom/aces/tv/Splash;->getBaseContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "activity"

    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/app/ActivityManager;

    .line 673
    const v1, 0x7fffffff

    invoke-virtual {v0, v1}, Landroid/app/ActivityManager;->getRunningTasks(I)Ljava/util/List;

    move-result-object v0

    .line 675
    invoke-interface {v0}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :cond_0
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v0

    if-eqz v0, :cond_1

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/app/ActivityManager$RunningTaskInfo;

    .line 676
    iget-object v0, v0, Landroid/app/ActivityManager$RunningTaskInfo;->topActivity:Landroid/content/ComponentName;

    invoke-virtual {v0}, Landroid/content/ComponentName;->toString()Ljava/lang/String;

    move-result-object v0

    const-string v3, "ComponentInfo{org.xbmc.kodi/org.xbmc.kodi.Main}"

    invoke-virtual {v0, v3}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_0

    .line 679
    invoke-virtual {p0}, Lcom/aces/tv/Splash;->startXBMC()V

    .line 781
    :goto_0
    return-void

    .line 683
    :cond_1
    iget-object v0, p0, Lcom/aces/tv/Splash;->mStateMachine:Lcom/aces/tv/Splash$StateMachine;

    const/4 v1, 0x2

    invoke-virtual {v0, v1}, Lcom/aces/tv/Splash$StateMachine;->sendEmptyMessage(I)Z

    .line 685
    const-string v0, ""

    .line 688
    :try_start_0
    invoke-virtual {p0}, Lcom/aces/tv/Splash;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    .line 689
    const/high16 v3, 0x7f040000

    invoke-virtual {v1, v3}, Landroid/content/res/Resources;->openRawResource(I)Ljava/io/InputStream;

    move-result-object v1

    .line 690
    new-instance v3, Ljava/util/Properties;

    invoke-direct {v3}, Ljava/util/Properties;-><init>()V

    .line 691
    invoke-virtual {v3, v1}, Ljava/util/Properties;->load(Ljava/io/InputStream;)V

    .line 692
    const-string v1, "native_arch"

    invoke-virtual {v3, v1}, Ljava/util/Properties;->getProperty(Ljava/lang/String;)Ljava/lang/String;
    :try_end_0
    .catch Landroid/content/res/Resources$NotFoundException; {:try_start_0 .. :try_end_0} :catch_0
    .catch Ljava/io/IOException; {:try_start_0 .. :try_end_0} :catch_1

    move-result-object v0

    .line 704
    :goto_1
    sget-object v5, Landroid/os/Build;->SUPPORTED_ABIS:[Ljava/lang/String;

    move v1, v2

    move v3, v2

    .line 705
    :goto_2
    array-length v6, v5

    if-ge v1, v6, :cond_3

    .line 707
    const-string v6, "Kodi"

    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    const-string v8, "ABI: "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    aget-object v8, v5, v1

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v7

    invoke-static {v6, v7}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    .line 708
    aget-object v6, v5, v1

    invoke-virtual {v6, v0}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v6

    if-eqz v6, :cond_2

    move v3, v4

    .line 705
    :cond_2
    add-int/lit8 v1, v1, 0x1

    goto :goto_2

    .line 693
    :catch_0
    move-exception v1

    .line 694
    const-string v1, "Cannot find properties file"

    iput-object v1, p0, Lcom/aces/tv/Splash;->mErrorMsg:Ljava/lang/String;

    .line 695
    const-string v1, "Kodi"

    iget-object v3, p0, Lcom/aces/tv/Splash;->mErrorMsg:Ljava/lang/String;

    invoke-static {v1, v3}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    .line 696
    iput v4, p0, Lcom/aces/tv/Splash;->mState:I

    goto :goto_1

    .line 697
    :catch_1
    move-exception v1

    .line 698
    const-string v1, "Failed to open properties file"

    iput-object v1, p0, Lcom/aces/tv/Splash;->mErrorMsg:Ljava/lang/String;

    .line 699
    const-string v1, "Kodi"

    iget-object v3, p0, Lcom/aces/tv/Splash;->mErrorMsg:Ljava/lang/String;

    invoke-static {v1, v3}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    .line 700
    iput v4, p0, Lcom/aces/tv/Splash;->mState:I

    goto :goto_1

    .line 715
    :cond_3
    if-nez v3, :cond_4

    .line 717
    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "This package is not compatible with your device ("

    invoke-virtual {v1, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    const-string v3, ").\nPlease check the <a href=\"http://wiki.kodi.tv/index.php?title=XBMC_for_Android_specific_FAQ\">Kodi Android wiki</a> for more information."

    invoke-virtual {v1, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    iput-object v1, p0, Lcom/aces/tv/Splash;->mErrorMsg:Ljava/lang/String;

    .line 718
    const-string v1, "Kodi"

    iget-object v3, p0, Lcom/aces/tv/Splash;->mErrorMsg:Ljava/lang/String;

    invoke-static {v1, v3}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    .line 719
    iput v4, p0, Lcom/aces/tv/Splash;->mState:I

    .line 722
    :cond_4
    iget v1, p0, Lcom/aces/tv/Splash;->mState:I

    if-eq v1, v4, :cond_5

    .line 723
    const-string v1, "arm"

    invoke-virtual {v0, v1}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_5

    .line 725
    invoke-direct {p0}, Lcom/aces/tv/Splash;->ParseCpuFeature()Z

    move-result v0

    .line 727
    if-nez v0, :cond_8

    .line 728
    const-string v0, "Error! Cannot parse CPU features."

    iput-object v0, p0, Lcom/aces/tv/Splash;->mErrorMsg:Ljava/lang/String;

    .line 729
    const-string v0, "Kodi"

    iget-object v1, p0, Lcom/aces/tv/Splash;->mErrorMsg:Ljava/lang/String;

    invoke-static {v0, v1}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    .line 730
    iput v4, p0, Lcom/aces/tv/Splash;->mState:I

    .line 742
    :cond_5
    :goto_3
    const-string v0, "Kodi"

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "External storage = "

    invoke-virtual {v1, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-static {}, Landroid/os/Environment;->getExternalStorageDirectory()Ljava/io/File;

    move-result-object v3

    invoke-virtual {v3}, Ljava/io/File;->getAbsolutePath()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v1, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    const-string v3, "; state = "

    invoke-virtual {v1, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-static {}, Landroid/os/Environment;->getExternalStorageState()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v1, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 743
    const-string v0, "mounted"

    invoke-static {}, Landroid/os/Environment;->getExternalStorageState()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_6

    .line 744
    iput-boolean v4, p0, Lcom/aces/tv/Splash;->mExternalStorageChecked:Z

    .line 746
    :cond_6
    iget v0, p0, Lcom/aces/tv/Splash;->mState:I

    if-eq v0, v4, :cond_7

    iget-boolean v0, p0, Lcom/aces/tv/Splash;->mExternalStorageChecked:Z

    if-eqz v0, :cond_7

    .line 747
    const/4 v0, 0x3

    iput v0, p0, Lcom/aces/tv/Splash;->mState:I

    .line 749
    invoke-direct {p0}, Lcom/aces/tv/Splash;->SetupEnvironment()V

    .line 750
    invoke-direct {p0}, Lcom/aces/tv/Splash;->MigrateUserData()V

    .line 752
    iget v0, p0, Lcom/aces/tv/Splash;->mState:I

    if-eq v0, v9, :cond_7

    iget v0, p0, Lcom/aces/tv/Splash;->mState:I

    if-eq v0, v4, :cond_7

    iget-object v0, p0, Lcom/aces/tv/Splash;->fXbmcHome:Ljava/io/File;

    invoke-virtual {v0}, Ljava/io/File;->exists()Z

    move-result v0

    if-eqz v0, :cond_7

    iget-object v0, p0, Lcom/aces/tv/Splash;->fXbmcHome:Ljava/io/File;

    invoke-virtual {v0}, Ljava/io/File;->lastModified()J

    move-result-wide v0

    iget-object v3, p0, Lcom/aces/tv/Splash;->fPackagePath:Ljava/io/File;

    invoke-virtual {v3}, Ljava/io/File;->lastModified()J

    move-result-wide v6

    cmp-long v0, v0, v6

    if-ltz v0, :cond_7

    iget-boolean v0, p0, Lcom/aces/tv/Splash;->mInstallLibs:Z

    if-nez v0, :cond_7

    .line 753
    iput v10, p0, Lcom/aces/tv/Splash;->mState:I

    .line 754
    iput-boolean v4, p0, Lcom/aces/tv/Splash;->mCachingDone:Z

    .line 758
    :cond_7
    iget v0, p0, Lcom/aces/tv/Splash;->mState:I

    if-eq v0, v9, :cond_b

    iget v0, p0, Lcom/aces/tv/Splash;->mState:I

    if-eq v0, v4, :cond_b

    iget-boolean v0, p0, Lcom/aces/tv/Splash;->mCachingDone:Z

    if-eqz v0, :cond_b

    iget-boolean v0, p0, Lcom/aces/tv/Splash;->mExternalStorageChecked:Z

    if-eqz v0, :cond_b

    .line 759
    invoke-virtual {p0}, Lcom/aces/tv/Splash;->startXBMC()V

    goto/16 :goto_0

    .line 732
    :cond_8
    const-string v0, "neon"

    invoke-direct {p0, v0}, Lcom/aces/tv/Splash;->CheckCpuFeature(Ljava/lang/String;)Z

    move-result v0

    if-nez v0, :cond_9

    const-string v0, "aarch64"

    invoke-direct {p0, v0}, Lcom/aces/tv/Splash;->CheckCpuFeature(Ljava/lang/String;)Z

    move-result v0

    if-nez v0, :cond_9

    const-string v0, "asimd"

    invoke-direct {p0, v0}, Lcom/aces/tv/Splash;->CheckCpuFeature(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_a

    :cond_9
    move v0, v4

    .line 733
    :goto_4
    if-nez v0, :cond_5

    .line 734
    const-string v0, "This Kodi package is not compatible with your device (NEON).\nPlease check the <a href=\"http://wiki.kodi.tv/index.php?title=XBMC_for_Android_specific_FAQ\">Kodi Android wiki</a> for more information."

    iput-object v0, p0, Lcom/aces/tv/Splash;->mErrorMsg:Ljava/lang/String;

    .line 735
    const-string v0, "Kodi"

    iget-object v1, p0, Lcom/aces/tv/Splash;->mErrorMsg:Ljava/lang/String;

    invoke-static {v0, v1}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    .line 736
    iput v4, p0, Lcom/aces/tv/Splash;->mState:I

    goto/16 :goto_3

    :cond_a
    move v0, v2

    .line 732
    goto :goto_4

    .line 763
    :cond_b
    const v0, 0x7f030001

    invoke-virtual {p0, v0}, Lcom/aces/tv/Splash;->setContentView(I)V

    .line 764
    const v0, 0x7f060003

    invoke-virtual {p0, v0}, Lcom/aces/tv/Splash;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/ProgressBar;

    iput-object v0, p0, Lcom/aces/tv/Splash;->mProgress:Landroid/widget/ProgressBar;

    .line 765
    const v0, 0x7f060004

    invoke-virtual {p0, v0}, Lcom/aces/tv/Splash;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/TextView;

    iput-object v0, p0, Lcom/aces/tv/Splash;->mTextView:Landroid/widget/TextView;

    .line 767
    iget v0, p0, Lcom/aces/tv/Splash;->mState:I

    if-eq v0, v9, :cond_c

    iget v0, p0, Lcom/aces/tv/Splash;->mState:I

    if-ne v0, v4, :cond_d

    .line 768
    :cond_c
    iget-object v0, p0, Lcom/aces/tv/Splash;->mStateMachine:Lcom/aces/tv/Splash$StateMachine;

    iget v1, p0, Lcom/aces/tv/Splash;->mState:I

    invoke-virtual {v0, v1}, Lcom/aces/tv/Splash$StateMachine;->sendEmptyMessage(I)Z

    goto/16 :goto_0

    .line 772
    :cond_d
    iget-boolean v0, p0, Lcom/aces/tv/Splash;->mExternalStorageChecked:Z

    if-nez v0, :cond_e

    .line 773
    invoke-virtual {p0}, Lcom/aces/tv/Splash;->startWatchingExternalStorage()V

    .line 774
    iget-object v0, p0, Lcom/aces/tv/Splash;->mStateMachine:Lcom/aces/tv/Splash$StateMachine;

    const/4 v1, 0x7

    invoke-virtual {v0, v1}, Lcom/aces/tv/Splash$StateMachine;->sendEmptyMessage(I)Z

    goto/16 :goto_0

    .line 776
    :cond_e
    iget-boolean v0, p0, Lcom/aces/tv/Splash;->mCachingDone:Z

    if-nez v0, :cond_f

    .line 777
    new-instance v0, Lcom/aces/tv/Splash$FillCache;

    invoke-direct {v0, p0, p0}, Lcom/aces/tv/Splash$FillCache;-><init>(Lcom/aces/tv/Splash;Lcom/aces/tv/Splash;)V

    new-array v1, v2, [Ljava/lang/Void;

    invoke-virtual {v0, v1}, Lcom/aces/tv/Splash$FillCache;->execute([Ljava/lang/Object;)Landroid/os/AsyncTask;

    goto/16 :goto_0

    .line 779
    :cond_f
    iget-object v0, p0, Lcom/aces/tv/Splash;->mStateMachine:Lcom/aces/tv/Splash$StateMachine;

    invoke-virtual {v0, v10}, Lcom/aces/tv/Splash$StateMachine;->sendEmptyMessage(I)Z

    goto/16 :goto_0
.end method

.method public showErrorDialog(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V
    .locals 3

    .prologue
    .line 406
    iget-object v0, p0, Lcom/aces/tv/Splash;->myAlertDialog:Landroid/app/AlertDialog;

    if-eqz v0, :cond_0

    iget-object v0, p0, Lcom/aces/tv/Splash;->myAlertDialog:Landroid/app/AlertDialog;

    invoke-virtual {v0}, Landroid/app/AlertDialog;->isShowing()Z

    move-result v0

    if-eqz v0, :cond_0

    .line 427
    :goto_0
    return-void

    .line 409
    :cond_0
    new-instance v0, Landroid/app/AlertDialog$Builder;

    invoke-direct {v0, p1}, Landroid/app/AlertDialog$Builder;-><init>(Landroid/content/Context;)V

    .line 410
    invoke-virtual {v0, p2}, Landroid/app/AlertDialog$Builder;->setTitle(Ljava/lang/CharSequence;)Landroid/app/AlertDialog$Builder;

    .line 411
    const v1, 0x1080027

    invoke-virtual {v0, v1}, Landroid/app/AlertDialog$Builder;->setIcon(I)Landroid/app/AlertDialog$Builder;

    .line 412
    invoke-static {p3}, Landroid/text/Html;->fromHtml(Ljava/lang/String;)Landroid/text/Spanned;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/app/AlertDialog$Builder;->setMessage(Ljava/lang/CharSequence;)Landroid/app/AlertDialog$Builder;

    .line 413
    const-string v1, "Exit"

    new-instance v2, Lcom/aces/tv/Splash$1;

    invoke-direct {v2, p0, p1}, Lcom/aces/tv/Splash$1;-><init>(Lcom/aces/tv/Splash;Landroid/app/Activity;)V

    invoke-virtual {v0, v1, v2}, Landroid/app/AlertDialog$Builder;->setPositiveButton(Ljava/lang/CharSequence;Landroid/content/DialogInterface$OnClickListener;)Landroid/app/AlertDialog$Builder;

    .line 420
    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/app/AlertDialog$Builder;->setCancelable(Z)Landroid/app/AlertDialog$Builder;

    .line 421
    invoke-virtual {v0}, Landroid/app/AlertDialog$Builder;->create()Landroid/app/AlertDialog;

    move-result-object v0

    iput-object v0, p0, Lcom/aces/tv/Splash;->myAlertDialog:Landroid/app/AlertDialog;

    .line 422
    iget-object v0, p0, Lcom/aces/tv/Splash;->myAlertDialog:Landroid/app/AlertDialog;

    invoke-virtual {v0}, Landroid/app/AlertDialog;->show()V

    .line 425
    iget-object v0, p0, Lcom/aces/tv/Splash;->myAlertDialog:Landroid/app/AlertDialog;

    const v1, 0x102000b

    invoke-virtual {v0, v1}, Landroid/app/AlertDialog;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/TextView;

    invoke-static {}, Landroid/text/method/LinkMovementMethod;->getInstance()Landroid/text/method/MovementMethod;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setMovementMethod(Landroid/text/method/MovementMethod;)V

    goto :goto_0
.end method

.method startWatchingExternalStorage()V
    .locals 2

    .prologue
    .line 635
    new-instance v0, Lcom/aces/tv/Splash$2;

    invoke-direct {v0, p0}, Lcom/aces/tv/Splash$2;-><init>(Lcom/aces/tv/Splash;)V

    iput-object v0, p0, Lcom/aces/tv/Splash;->mExternalStorageReceiver:Landroid/content/BroadcastReceiver;

    .line 642
    new-instance v0, Landroid/content/IntentFilter;

    invoke-direct {v0}, Landroid/content/IntentFilter;-><init>()V

    .line 643
    const-string v1, "android.intent.action.MEDIA_MOUNTED"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    .line 644
    const-string v1, "android.intent.action.MEDIA_REMOVED"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    .line 645
    const-string v1, "android.intent.action.MEDIA_SHARED"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    .line 646
    const-string v1, "android.intent.action.MEDIA_UNMOUNTABLE"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    .line 647
    const-string v1, "android.intent.action.MEDIA_UNMOUNTED"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    .line 648
    const-string v1, "file"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addDataScheme(Ljava/lang/String;)V

    .line 649
    iget-object v1, p0, Lcom/aces/tv/Splash;->mExternalStorageReceiver:Landroid/content/BroadcastReceiver;

    invoke-virtual {p0, v1, v0}, Lcom/aces/tv/Splash;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;)Landroid/content/Intent;

    .line 650
    return-void
.end method

.method protected startXBMC()V
    .locals 2

    .prologue
    .line 659
    invoke-virtual {p0}, Lcom/aces/tv/Splash;->getIntent()Landroid/content/Intent;

    move-result-object v0

    .line 660
    const-class v1, Lcom/aces/tv/Main;

    invoke-virtual {v0, p0, v1}, Landroid/content/Intent;->setClass(Landroid/content/Context;Ljava/lang/Class;)Landroid/content/Intent;

    .line 661
    const/high16 v1, 0x1000000

    invoke-virtual {v0, v1}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    .line 662
    invoke-virtual {p0, v0}, Lcom/aces/tv/Splash;->startActivity(Landroid/content/Intent;)V

    .line 663
    invoke-virtual {p0}, Lcom/aces/tv/Splash;->finish()V

    .line 664
    return-void
.end method

.method stopWatchingExternalStorage()V
    .locals 1

    .prologue
    .line 653
    iget-object v0, p0, Lcom/aces/tv/Splash;->mExternalStorageReceiver:Landroid/content/BroadcastReceiver;

    if-eqz v0, :cond_0

    .line 654
    iget-object v0, p0, Lcom/aces/tv/Splash;->mExternalStorageReceiver:Landroid/content/BroadcastReceiver;

    invoke-virtual {p0, v0}, Lcom/aces/tv/Splash;->unregisterReceiver(Landroid/content/BroadcastReceiver;)V

    .line 655
    :cond_0
    return-void
.end method

.method updateExternalStorageState()V
    .locals 4

    .prologue
    .line 625
    invoke-static {}, Landroid/os/Environment;->getExternalStorageState()Ljava/lang/String;

    move-result-object v0

    .line 626
    const-string v1, "Kodi"

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "External storage = "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-static {}, Landroid/os/Environment;->getExternalStorageDirectory()Ljava/io/File;

    move-result-object v3

    invoke-virtual {v3}, Ljava/io/File;->getAbsolutePath()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, "; state = "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 627
    const-string v1, "mounted"

    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_0

    .line 628
    iget-object v0, p0, Lcom/aces/tv/Splash;->mStateMachine:Lcom/aces/tv/Splash$StateMachine;

    const/16 v1, 0x8

    invoke-virtual {v0, v1}, Lcom/aces/tv/Splash$StateMachine;->sendEmptyMessage(I)Z

    .line 632
    :goto_0
    return-void

    .line 630
    :cond_0
    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/aces/tv/Splash;->mExternalStorageChecked:Z

    goto :goto_0
.end method
